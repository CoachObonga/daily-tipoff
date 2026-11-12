#!/usr/bin/env python3
"""Validate Daily Tip-Off issue HTML against its source-verification manifest.

Usage:
 python scripts/validate_issue.py reports/2026-11-13.html qa/2026-11-13.json

Manifest structure (written by publisher after independent schedule enumeration):
{
 "issue_date":"2026-11-13","results_date":"2026-11-12","issue_number":11,
 "expected_games":[{"key":"2026-11-12|Away|Home","status":"final","sources":["https://...","https://..."]},...],
 "reported_games":[{"key":"2026-11-12|Away|Home","status":"final","sources":["https://...","https://..."]},...],
 "today_expected_games":["Away|Home",...],
 "today_reported_games":["Away|Home",...],
 "latest_poll_date":"2026-11-09"
}
Set "status" to "postponed" or "cancelled" when appropriate; final scores require
at least two distinct independent source URLs. This tool verifies evidence
STRUCTURE and matchup-set reconciliation, not truth of external websites.
"""
import json, re, sys
from pathlib import Path
from html import unescape

SECTIONS = ["alabama","national","sec","trends","health","rankings","scores","lookahead","sources"]
POLL_COLUMNS = ["Rank","Team","Previous Rank","Movement","Yesterday's Result"]

def plain(markup):
    return unescape(re.sub(r"<[^>]+>", "", markup)).strip()

def extract_table(html, table_id):
    hit = re.search(r'<table\b[^>]*\bid=["\\']'+re.escape(table_id)+r'["\\'][^>]*>(.*?)</table>',html,re.I|re.S)
    if not hit: raise ValueError("Missing table: " + table_id)
    return hit.group(1)

def cells(row, tag):
    return [plain(x) for x in re.findall(r"<"+tag+r"\b[^>]*>(.*?)</"+tag+r">",row,re.I|re.S)]

def rows(markup):
    return re.findall(r"<tr\b[^>]*>(.*?)</tr>",markup,re.I|re.S)

def validate(html, manifest):
    errors=[]
    def require(condition, msg):
        if not condition: errors.append(msg)

    require("THE DAILY TIP-OFF" in plain(html).upper(),"Missing publication title")
    number=str(manifest.get("issue_number",""))
    require(bool(re.search(r"ISSUE\s*0*"+re.escape(number)+r"\b",plain(html),re.I)),"Issue number missing or wrong")
    require(manifest.get("issue_date","") in html,"Issue date missing")
    require(manifest.get("results_date","") in html or "Results from" in html,"Results date missing")
    for sec in SECTIONS:
        require(bool(re.search(r'\bid=["\\']'+sec+r'["\\']',html,re.I)),f"Missing fixed section id: {sec}")

    try:
        poll=extract_table(html,"ap-top25")
        rr=rows(poll)
        headers=cells(rr[0],"th") if rr else []
        require(headers==POLL_COLUMNS,f"AP columns changed: {headers}")
        entries=[cells(row,"td") for row in rr[1:]]
        require(len(entries)==25,f"Expected 25 AP entries, saw {len(entries)}")
        team_names=[]
        for i,entry in enumerate(entries,1):
            require(len(entry)==5,f"AP row {i} should contain five columns")
            if len(entry)<5: continue
            require(entry[0]==str(i),f"AP rank {i} invalid: {entry[0]}")
            require(len(entry[1])>=3,f"AP team at rank {i} appears truncated")
            team_names.append(entry[1].casefold())
            result=entry[4].strip()
            require(result=="Idle" or bool(re.search(r"^[WL]\s+(?:vs\.?|at)\s+\S.{2,}\s+\d+\s*[-–]\s*\d+",result,re.I)),
                f"AP result at rank {i} missing opponent or score: {result!r}")
        require(len(team_names)==len(set(team_names)),"Duplicate AP team")
        require(manifest.get("latest_poll_date","") in html,"Poll publication date absent")
    except ValueError as exc: errors.append(str(exc))

    expected=manifest.get("expected_games",[])
    reported=manifest.get("reported_games",[])
    ek=[g.get("key") for g in expected]
    rk=[g.get("key") for g in reported]
    require(bool(ek),"Manifest missing independent national schedule enumeration")
    require(len(ek)==len(set(ek)),"Duplicate expected game keys")
    require(len(rk)==len(set(rk)),"Duplicate reported game keys")
    require(set(ek)==set(rk),f"National results slate not reconciled: missing={sorted(set(ek)-set(rk))}, extra={sorted(set(rk)-set(ek))}")
    for g in reported:
        src=g.get("sources",[])
        require(len(set(src))>=2 if g.get("status")=="final" else bool(src),
          f"Insufficient independent sources for {g.get('key')}")
        require(all(str(u).startswith("https://") for u in src),f"Non-HTTPS source URL for {g.get('key')}")
    tx=manifest.get("today_expected_games",[])
    tr=manifest.get("today_reported_games",[])
    require(bool(tx),"Missing independent today's game list")
    require(len(tx)==len(set(tx)),"Duplicate look-ahead expected matchup")
    require(set(tx)==set(tr),f"Look Ahead mismatch: missing={sorted(set(tx)-set(tr))}, extra={sorted(set(tr)-set(tx))}")
    require("Where to Watch" in html,"Look Ahead broadcast column missing")
    if errors: raise ValueError("\n".join(errors))
    return len(ek), len(tx)

if __name__=="__main__":
    if len(sys.argv)!=3:
        sys.exit("Usage: python scripts/validate_issue.py report.html qa/YYYY-MM-DD.json")
    h=Path(sys.argv[1]).read_text(encoding="utf-8")
    m=json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    try:
        games,look=validate(h,m)
    except ValueError as e:
        print("FAIL: Daily Tip-Off publication quality gate\n"+str(e),file=sys.stderr)
        sys.exit(1)
    print(f"PASS: fixed layout, AP25, {games} reconciled results and {look} Look Ahead games")
