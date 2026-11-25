# I went through 113 GTM and RevOps job listings so you don't have to

For you if you're in GTM or RevOps, or moving into that work, and you want a clear picture of what listings actually ask you to *do* in late 2026, heading into 2027.

Builder's Desk · by Mo Bamidele

## What this is

113 real job listings in one sheet, a count of the capabilities they ask for, and a short 2027 skill checklist in priority order. This is not a list of jobs to apply to. It is a skills map.

The mid-November kit counted *tools* in 100 LinkedIn posts (CRM, Clay, n8n, Zapier, APIs, SQL). This one counts *what you should be able to do*, from official career pages, in a fresh window.

## The sample (read this first)

- 113 public listings, collected read-only on 25 Nov 2026 (Africa/Lagos)
- Posted between 14 Oct and 24 Nov 2026 (about the last six weeks)
- 75 companies. Sources: 51 Ashby, 47 Greenhouse, 15 Lever, all from the employer's own job board
- Role mix: 35 RevOps / Revenue Operations, 26 Sales Operations, 22 GTM Engineer, 11 GTM / Revenue Systems, 8 GTM Operations, 7 Marketing Operations, 4 other GTM/RevOps systems roles
- Seniority: 38 unstated or mid, 34 manager, 12 senior, 12 senior/staff, 10 director, 5 leadership (head/VP), 2 junior
- 33 of the 113 listed a cash pay figure on the posting
- Location is whatever the employer published. This is a worldwide sample, not a remote-only list
- Jobgether listings are partner-company ads hosted on Jobgether. Where the same specialist role was posted in several countries with the same description, it is counted once
- One "GTM Engineer, Web" listing (Toast) was dropped because the body was a web-production role, not GTM or RevOps systems work
- Official multi-city copies of the same employer role (for example Braze in New York, San Francisco and Chicago) are counted separately, the same way the mid-November kit treated city copies

## How the counting was done

- A case-insensitive search of the title and the full description
- A listing counts once per capability if the pattern appears anywhere, including a "nice to have" section
- Two 2027-forward capabilities use a tighter pattern, on purpose:
  - **Build, ship or run AI agents** counts only listings that ask you to build, ship, run, deploy or manage agents or agentic workflows. A company slogan like "the agentic enterprise" is not enough
  - **AI evals or guardrails** counts evals, guardrails, human-in-the-loop, or "validate AI outputs" — not a generic "vendor evaluation"
- This is one sample and a keyword count. Treat it as a rough guide to what is being asked for, not a market study
- The mid-November kit was 100 LinkedIn posts (45 GTM Engineer, 35 RevOps / Revenue Operations Engineer, 20 Growth / Outbound Engineer), collected 10 Nov 2026. This sample has more Revenue Operations and Sales Operations listings, so tool-to-tool comparisons are only fair where the category still matches, and even then the mix is different

## What's inside

- `listings.csv`: all 113 listings with the link, company, role type, seniority, location, date posted, pay where listed, and the capabilities each one asks for
- `skills-breakdown.csv`: every count, with the split by role type and the exact match pattern
- `checklist.md`: the 2027 skill checklist, in order of how often the capability is asked for, plus a short start-here path
- `count_skills.py` and `capability-patterns.json`: rerun the count on `postings.json`, or on your own file in the same format
- `postings.json`: the title, metadata and description used for the count, so you can rerun it

## How to use it

1. Open `checklist.md` and tick what you already do at work
2. Start with the gaps at the top of the list, then add the 2027-forward ones (agents, evals, MCP) once the table stakes are in place
3. Save one small build (a CRM workflow, a routing rule, a tiny agent with a check on the output) and write down what changed. That is your proof

## A few headline counts (out of 113)

Table stakes:

- 95 ask for HubSpot or Salesforce (84%). 85 name Salesforce, 33 name HubSpot
- 89 ask for reporting, dashboards or forecasting (79%)
- 69 mention SQL or a data warehouse (61%). 59 mention SQL itself (52%)
- 62 ask you to enrich, score or route leads or accounts (55%)

The newer asks:

- 54 name Claude, ChatGPT, GPT, OpenAI or Anthropic (48%) — similar to 50 of 100 in the mid-November LinkedIn sample
- 36 ask you to build, ship or run AI agents or agentic workflows (32%)
- 11 ask for AI evals or guardrails around the output (10%)
- 10 name MCP, the Model Context Protocol (9%)
- 10 name Claude Code, Cursor, or similar AI coding tools (9%)

Where a mid-November comparison is fair (same regex, different sample):

- CRM: 62 of 100 then, 95 of 113 now
- Reporting / dashboards / forecasting: 62 of 100 then, 89 of 113 now
- SQL: 51 of 100 then, 59 of 113 now
- LLMs named: 50 of 100 then, 54 of 113 now
- Clay: 33 of 100 then, 36 of 113 now
- Python, JavaScript or TypeScript: 46 of 100 then, 26 of 113 now. This sample is heavier on RevOps and Sales Operations, so do not read that drop as "Python is going away"

## Notes

- Counts do not tell you which skills are required and which are nice to have. Read the requirements section of any listing you care about
- Pay is included only where the posting listed a cash figure, cleaned from the board's compensation field. Equity is not treated as cash pay
- Use your own numbers once you have them. Collect 20 to 30 listings for the exact role you want and rerun the script
