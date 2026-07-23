# Workflow Doc: [Workflow Name]

Most workflow docs are just a list of clicks: click here, then here, then here. That's useful for about a month, until the workflow changes and the doc goes stale. What actually holds up over time is writing down *why this exists* and *what happens if it breaks*, not just the steps. If someone reads this and still can't tell you why this workflow matters, it's not finished yet.

**Owner:** [Name]
**Last updated:** [YYYY-MM-DD]
**Status:** Active / No longer used / Needs a rework

---

## Why this exists

What problem does this solve? What gets worse or slower if it didn't exist?

[2-4 plain sentences]

## What kicks it off

[A new lead coming in? A scheduled run? Someone clicking a button? A form being filled out?]

## What it actually does

1. [Step 1, and which tool it happens in]
2. [Step 2]
3. [Step 3]
4. ...

## Tools involved

| Tool | What it does here |
|---|---|
| [Tool 1] | |
| [Tool 2] | |

## What it needs to run

[What data or trigger does this depend on?]

## What comes out of it

[What does it produce, where does it go, who or what uses it next?]

## Where it breaks down

- [e.g. "Fails if the lead doesn't have a company website listed"]
- [Another case]

## If this breaks

[Who notices, and how? Is there a backup way to do this by hand while it's down? If the answer is "nobody would notice," that's worth flagging on the Technical Debt Scorecard.]

## Related

- Related decision log entry (why it's built this way): [link]
- Related mistake log entries (past times this broke): [link]
- Workflows upstream or downstream of this one: [link]

## Changes over time

| Date | What changed | Who changed it |
|---|---|---|
| [YYYY-MM-DD] | First version | [Name] |

---
*If you change this workflow, update this doc in the same sitting, not "later." Later is how workflows end up with no docs in the first place.*
