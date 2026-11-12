# I scraped 100 GTM jobs so you don't have to

For you if you're moving into GTM or want a GTM job.

Builder's Desk · by Mo Bamidele, GTM Engineer

## What this is
All 100 real job postings in one sheet, a count of which skills and tools show up in them, plus a one-page checklist and a 4-week plan for someone moving from sales into a GTM Engineer, RevOps or Growth/Outbound role.

## The sample (read this first)
- 100 public LinkedIn job postings, collected read-only on Nov 10, 2026
- Roles: 45 GTM Engineer, 35 RevOps / Revenue Operations Engineer, 20 Growth / Outbound Engineer
- Posted between Oct 16 and Nov 10, 2026. 88 different companies. Some companies posted the same role in more than one city, and those are counted separately
- Not all are remote. The word "remote" appears in 33 of the 100, so check each posting
- Counting method: a case-insensitive keyword match on the title and description. A posting counts once per skill if the word appears anywhere, including in the "nice to have" part or the company blurb
- This is one sample and a keyword count. Treat it as a rough guide to what is asked for, not a market study

## What's inside
- `100-gtm-jobs.csv`: all 100 jobs with title, company, location, date posted, role type, salary where listed, the tools each one mentions, and the link
- `checklist.md`: the one-page checklist
- `learning-plan-4-weeks.md`: a small weekly plan, one thing to build each week
- `skills-from-100-postings.csv`: every count, with the split by role (GTM 45, RevOps 35, Growth/Outbound 20) and the exact match pattern used
- `count_skills.py`: the script that produced the counts. Run `python3 count_skills.py your-postings.json` on a file of postings in the same format (fields: title, description, role_category) to rerun it on postings you collect yourself

## How to use it
1. Open `checklist.md` and tick what you already do at work
2. Pick the first gap and follow the plan for week 1
3. Save what you build in a folder with a short write-up. That is your proof

## Notes
- Counts do not tell you which skills are required and which are nice to have. Read the requirements section of each posting you care about
- Use your own numbers once you have them. Collect 20 to 30 postings for the exact role you want and rerun the script
