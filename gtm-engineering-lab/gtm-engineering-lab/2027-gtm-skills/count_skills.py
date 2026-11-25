"""Recount capabilities on the 113 postings in postings.json.

Method: case-insensitive regex on title + description. A listing counts
once per capability if the pattern appears anywhere, including a
nice-to-have section or company blurb.

The 'Build, ship or run AI agents' and 'AI evals or guardrails' patterns
are tighter than a bare word search, so company slogans like 'the agentic
enterprise' do not count unless the listing also asks you to build, run or
guardrail agents. See capability-patterns.json for every pattern.
"""
import csv, json, re, collections, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
postings = json.load(open(sys.argv[1] if len(sys.argv) > 1 else ROOT / "postings.json"))
CAPS = json.load(open(ROOT / "capability-patterns.json"))

def text(p):
    return (p.get("title") or "") + "\n" + (p.get("description") or "")

n = len(postings)
rows = []
for name, pat in CAPS.items():
    c = sum(bool(re.search(pat, text(p), re.I)) for p in postings)
    by = collections.Counter()
    for p in postings:
        if re.search(pat, text(p), re.I):
            by[p.get("role_category") or ""] += 1
    rows.append((name, c, by, pat))

for name, c, by, pat in sorted(rows, key=lambda x: -x[1]):
    print(f"{c:3d}/{n}  {c/n*100:5.1f}%  {name}")
