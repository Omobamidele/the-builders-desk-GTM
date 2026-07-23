# Workflow Doc: [Workflow Name]

> **Format note:** Most workflow docs are step lists — click here, then here, then here. That's a runbook, not documentation, and it goes stale the moment the workflow changes. This template borrows the core idea behind ADRs: the reader six months from now doesn't need to be told what buttons to click nearly as much as they need to know *why this exists* and *what happens if it breaks*. If someone reads this and still can't explain why they'd ever touch this workflow, it isn't done.

**Owner:** [Name / role]
**Last updated:** [YYYY-MM-DD]
**Status:** `Active` / `Deprecated` / `Needs rework`

---

## Purpose — why this exists

What business problem does this solve? What breaks or gets slower without it? This is the section most workflow docs skip — don't skip it.

[2-4 sentences.]

## Trigger

[What kicks this off? A new lead, a scheduled run, a manual click, a form submission?]

## What it does (steps)

1. [Step 1 — tool/system involved]
2. [Step 2]
3. [Step 3]
4. ...

## Tools / systems involved

| Tool | Role in this workflow |
|---|---|
| [Tool 1] | |
| [Tool 2] | |

## Inputs

[What data or trigger event does this need to run correctly?]

## Outputs

[What does this produce, where does it end up, who or what consumes it?]

## Edge cases / known limitations

- [Case 1 — e.g. "Breaks if the lead has no company domain"]
- [Case 2]

## What happens if this breaks

[Who notices, how, and what's the manual fallback while it's down? If there's no answer to this, that's a finding for the Technical Debt Scorecard.]

## Related

- Related Decision Log entry (why this workflow is built the way it is): [link]
- Related Mistake Log entries (past failures in this workflow): [link]
- Upstream / downstream workflows: [link]

## Change history

| Date | Change | Changed by |
|---|---|---|
| [YYYY-MM-DD] | Initial version | [Name] |

---
*If you modify this workflow, update this doc in the same change — not "later." "Later" is how workflows end up undocumented in the first place.*
