# THE DAILY TIP-OFF — CANONICAL EDITORIAL AND PUBLICATION STANDARD
Version 1.0 · Adopted November 12, 2026 · Applies to all future NCAA Division I MEN'S basketball issues.
This is the single layout and verification contract. Do not improvise section names or columns from day to day. Only change format on explicit user approval.

## A. Reporting window
Issue date = today's America/Chicago calendar date, and results date = preceding America/Chicago calendar date. Include every NCAA D-I men's game on the results date (including D-I vs non-D-I); do not conflate NBA, women's basketball, or another date. Maintain issue numbers consecutively; derive from last successfully published issue, not from guesswork.

## B. Verified data pipeline — REQUIRED before writing prose
1. Enumerate the complete results-date matchup list from a primary nationwide scoreboard (ESPN NCAAM or NCAA.com; CBS Sports, FOX Sports and official athletics sites as secondary independent sources). Get all finals, scheduled/postponed/cancelled and late/night games. A single editorial search result is not a full slate.
2. Cross-check every matchup/final (both school names, winner/loser, score, OT) against an independent scoreboard or the official school/conference box score. Resolve discrepancies with the official game box score, preserving its URL and recording the discrepancy.
3. Store one normalized row per game keyed by date+away+home; never omit a game just because the article lacks player details. The verification manifest must record the independently enumerated expected game count, observed final/postponed count, source URL(s) and any still unresolved games. Compare the normalized set to the independently enumerated slate, not just count equality.
4. For Alabama and major featured games, use the official full box score for actual starters, roster positions, minutes, player totals, team stats and starter-versus-bench scoring. Confirm lineup from asterisks/starting indicators, not from projections. On game days before official starters have been announced, label 'Starting lineup: Awaiting official announcement.'
5. Independently enumerate today's full Look Ahead slate and tip times from a national schedule. Confirm TV/streaming for every matchup from ESPN/CBS or official broadcast listing. Display 'Not confirmed' ONLY in the individual broadcast cell when no reliable broadcast is published. Use CT consistently; label non-D-I opponents.
6. Use the current AP MEN'S poll from AP/credible poll mirror with release DATE; compare to the immediately prior poll. Verify exact 1–25 rankings. For all 25 teams, show result of covered day only after checking the completed slate: 'W vs [opponent] [team score]–[opp score]', 'L vs [opponent] ...', or 'Idle'. Never show a bare W/L+score without opponent. Add prior rank/movement and entrants/dropouts ONLY on first issue after a new poll, with sourced context of any dropout (do not claim inside knowledge of voters).
7. Review ALL 16 SEC teams for any losses, highlight every SEC loss explicitly with opponent and exact score. Review rolling 7-day and season trends across all D-I teams, including repeat upsets, road streaks, injuries and breakout players; verify every high-impact claim.
8. Maintain Health & Roster Watch every issue: Alabama, SEC, AP Top 25, emerging teams and major stars nationally. Date/time and source for injury/availability; if nothing verified, say 'No significant new confirmed updates' rather than inventing.
9. Save verified normalized score results and source URLs to the season Google Sheets archive, deduplicating by date+matchup. Cross-check retained running Alabama schedule/record with official sources.

## C. Full website layout — fixed order and fixed table schemas
Header: THE DAILY TIP-OFF · ISSUE ### · WEEKDAY DATE · Results from DATE · engaging specific headline.
1. ALABAMA BASKETBALL — record, last result, next game (time CT, venue, viewing), if played: official starting five, positions, all players MIN/PTS/REB/AST/STL/BLK/FG/3PT/FT, team stats, starter/bench points, game picture, season running W/L. If today Alabama plays: official starters if released, otherwise 'Awaiting official announcement'.
2. AROUND THE COUNTRY — largest results, ranked teams, surprising performances and why they matter.
3. SEC WATCH & LOSSES — 16-team roundup, explicitly acknowledge every loss, significant wins and trends.
4. BIG STORIES & SEASON TRENDS — multi-game development, record context and confirmed upset analysis.
5. HEALTH & ROSTER WATCH — always present; meaningful national/SEC/Alabama injuries and roster changes.
6. AP TOP 25 — EVERY day the same columns: Rank | Team | Previous Rank | Movement | Yesterday's Result (opponent & complete score, or Idle). Source and poll date above. Movement uses comparison of the most recent and prior published polls; use '—' only when prior ranking unavailable, never fabricate. On newly released polls add below table: Entered, Dropped Out (teams and context), Biggest Risers/Fallers. NEVER remove opponent/score column when poll changes.
7. VERIFIED NATIONAL SCORES ARCHIVE — searchable table for complete covered-day slate: Date | Away | Away Pts | Home | Home Pts | Status/OT | Source. Include all D-I program games, even non-D-I opponents. Historical archive remains cumulative in Sheets.
8. TODAY'S COMPLETE LOOK AHEAD — every scheduled D-I-program game, CT tipoff, away, home, TV/streaming, ranked/rivalry/upset flags as evidence permits.
9. SOURCES & COVERAGE CHECK — name coverage sources and results-date match-count reconciliation. Visible warning only when truly unresolved; don't advertise partial coverage as complete.
Headings and table columns NEVER change without explicit user approval. Use anchors/IDs: alabama, national, sec, trends, health, rankings, scores, lookahead, sources.

## D. Short HTML email layout — fixed
Masthead: THE DAILY TIP-OFF · ISSUE ###; WEEKDAY DATE; Results from DATE; headline.
Short Alabama lead, Around the Country, SEC Watch & National Trends (flag SEC losses), Health & Roster Watch (brief), Today's Featured Look Ahead (ONLY 3–5 best matchups with CT and Where to Watch). End with burgundy HTML anchor button labeled EXACTLY 'The Daily Tip-Off Full Report' linking to that date's deployed https://coachobonga.github.io/daily-tipoff/reports/YYYY-MM-DD.html. Never include the entire scoreboard or report inline; no HTML attachment. Send to all three: dylanchenoweth23@gmail.com, dchenoweth@merrimackhall.com, jschrimsher123@gmail.com.

## E. Release gate and failure recovery
Do NOT mark a national slate complete just because a few articles were found. Validate the canonical sections, AP 25 full names/ranks and matchup results, exact game-set reconciliation, source links, no duplicated games, times/TV, issue number and correct dates before publishing.
If national schedule cannot be enumerated or scores not reconciled, first retry with independent nationwide sources and official game pages. If still incomplete at deadline, publish an explicitly provisional edition with a concise data-gap note naming missing coverage and schedule a same-day repair; do not leave misleading 'complete' language. Avoid repeated 'unverified' labels on routine items that can be cross-checked; spend effort verifying them.
Publish dated HTML AND update index.html. Check GitHub Actions deployment for latest commit success, then send short email. If still deploying, 6:20 delivery-check task retries after status check; prevent duplicates via Gmail Sent lookup by issue/date and all recipients. Never silently abandon sending. The run must report actual successful/failed outcomes rather than planned actions.
Reference repository: CoachObonga/daily-tipoff; homepage https://coachobonga.github.io/daily-tipoff/.
