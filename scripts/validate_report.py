#!/usr/bin/env python3
"""Validate the AP Top 25 section in an HTML Daily Tip-Off report.
Usage: python scripts/validate_report.py reports/2026-11-05.html
Fails on broken ranks, truncated team names, duplicate teams or missing rows.
"""
import re, sys, pathlib, html

def validate(raw):
    section = re.search(r'<section\\b[^>]*\\bid=["\\\']rankings["\\\'][^>]*>(.*?)</section>', raw, re.I | re.S)
    if not section:
        raise ValueError("Missing rankings section")
    table = re.search(r'<table\\b[^>]*\\bid=["\\\']ap-top25["\\\'][^>]*>(.*?)</table>', section.group(1), re.I | re.S)
    if not table:
        raise ValueError("Missing labeled AP Top 25 table")
    body = re.search(r'<tbody[^>]*>(.*?)</tbody>', table.group(1), re.I | re.S)
    if not body:
        raise ValueError("Missing Top 25 table body")
    rows = re.findall(r'<tr[^>]*>(.*?)</tr>', body.group(1), re.I | re.S)
    if len(rows) != 25:
        raise ValueError(f"Expected 25 AP teams, received {len(rows)}")
    teams = []
    for rank, row in enumerate(rows, 1):
        cells = [html.unescape(re.sub(r'<[^>]+>', '', c).strip()) for c in re.findall(r'<td[^>]*>(.*?)</td>', row, re.I | re.S)]
        if len(cells) < 3:
            raise ValueError(f"Malformed row {rank}")
        if cells[0] != str(rank):
            raise ValueError(f"AP rank should be {rank}, got {cells[0]!r}")
        if len(cells[1]) < 3 or not any(c.isalpha() for c in cells[1]):
            raise ValueError(f"Truncated or invalid team at rank {rank}: {cells[1]!r}")
        teams.append(cells[1].casefold())
    if len(set(teams)) != 25:
        raise ValueError("Duplicate team in AP Top 25")
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python scripts/validate_report.py path/to/report.html")
    validate(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
    print("AP Top 25 validated: 25 unique teams, complete names, consecutive ranks 1–25.")
