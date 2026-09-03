# 🪜 The GTM Engineer Skill Ladder

Everyone with this title is not doing the same job.

A 2026 survey of 228 GTM Engineers (Maja Voje, Garrett Wolfe, and Alex Lindahl — the largest benchmark study of its kind) found that "GTM Engineer" is really three different jobs wearing one title. What separates them isn't the title, the company, or even years of experience. It's technical depth — specifically, whether you can code.

This isn't a salary post. It's a map: here's what each tier actually does day to day, and here's the specific, concrete thing that moves you from one to the next.

## The Three Tiers (What The Data Actually Shows)

### Tier 1 — Low-Code Operator
**What you do:** Connect existing tools. Manage enrichment pipelines. Run outbound programs using platforms built by someone else. The work is configuration, not construction.

**Typical tools:** Clay, Zapier, Make, Airtable, no-code workflow builders inside HubSpot or Salesforce.

**Where this tier sits:** This is the entry point for most people in the role, and it's a completely legitimate place to operate from. The survey's median base for this tier: **$90K**.

### Tier 2 — Mid-Level Technical Builder
**What you do:** Everything Tier 1 does, plus you can reach past the no-code layer when it hits a wall. You understand scripting, basic APIs, and how to shape data instead of just moving it.

**Typical tools:** Python or JavaScript basics, SQL fundamentals, direct API calls, Clay or HubSpot extended with your own scripts instead of waiting on a native feature.

**Where this tier sits:** The survey's median base: **$105K.**

### Tier 3 — High-Code Engineer
**What you do:** Build the infrastructure other people configure. Custom workflows, real data pipelines, sometimes replacing a paid vendor tool entirely because you built something that fits better.

**Typical tools:** Python, JavaScript, SQL, data warehouses (Snowflake, BigQuery), AI-assisted coding tools (Cursor, Claude Code — adoption among GTM Engineers is now approaching 70%).

**Where this tier sits:** The survey's median base: **$135K** — roughly a $40–45K premium over Tier 1, for the same job title.

## How To Climb The Ladder

Not generic advice — the specific gap the data points to at each step, with a real, free resource to actually go do it. No invented tutorials, no paywalled courses required.

### Tier 1 → Tier 2

**1. Learn to call an API yourself — not through a no-code connector.**
freeCodeCamp's free "APIs for Beginners" course covers the concept end to end, with hands-on Python and JavaScript examples.
→ https://www.freecodecamp.org/news/apis-for-beginners/

**2. Learn SQL — specifically joins.**
Most enrichment and CRM problems are data problems wearing a different costume. SQLZoo's free interactive JOIN tutorial runs real queries in your browser, no setup required.
→ https://sqlzoo.net/wiki/The_JOIN_operation

**3. Find one workflow you run entirely inside Clay, and extend it with a real API call.**
Clay's own HTTP API integration docs — the exact feature that lets you call any external API from inside a table when the native tool hits a wall.
→ https://university.clay.com/docs/http-api-integration-overview

### Tier 2 → Tier 3

**4. Build something that runs on a schedule, without you triggering it.**
GitHub's official docs on scheduled (cron) workflows — free to run on any repo, public repos get unlimited minutes.
→ https://docs.github.com/actions/using-workflows/workflow-syntax-for-github-actions

**5. Put a data warehouse in the middle of a workflow instead of passing data tool-to-tool.**
Google BigQuery's Sandbox — free, no credit card, no billing account required to start querying.
→ https://docs.cloud.google.com/bigquery/docs/sandbox

**6. Use an AI coding tool to build one small internal tool that replaces a step you currently pay a vendor for.**
Cursor, free tier, no card required — or Claude Code, Anthropic's own agentic coding tool.
→ https://cursor.com · https://code.claude.com/docs/en/overview

The pattern across both jumps is the same: stop waiting for the platform to add the feature, and build the missing piece yourself. Every link above is free to start.

## Where You Actually Stand

Reading tiers is one thing. Most people overestimate or underestimate which one they're actually in. `ladder.html` is a short self-check — answer honestly about what you currently do (not what you've read about), and it tells you your tier and the single next skill worth learning.

## Sources

**Data on the tiers and compensation:**
- *The 2026 State of GTM Engineering* — Maja Voje, Garrett Wolfe, Alex Lindahl. 228 respondents, 30+ countries. knowledge.gtmstrategist.com, March 2026.
- GTM Engineer Salary: Comprehensive 2026 Compensation Guide — Apollo.io, 2026.
- GTM Engineer: Role, Salary & Skills in 2026 — Prospeo, 2026.

**Learning resources linked above:**
- freeCodeCamp — APIs for Beginners
- SQLZoo — The JOIN Operation
- Clay University — HTTP API Integration Overview
- GitHub Docs — Workflow Syntax for GitHub Actions (Schedule)
- Google Cloud Docs — Try BigQuery Using the Sandbox
- Cursor · Claude Code (Anthropic)
