# Technical Debt Scorecard: [Workflow or Tool Stack Name]

"Technical debt" is a software term for shortcuts that made sense at the time but are now quietly slowing everyone down, the same way a small loan grows because nobody ever pays it back. This scorecard borrows an old software engineering idea (a guy named Martin Fowler wrote about this back in 2009) and applies it to GTM stacks, which usually have way more of this debt than anyone realizes.

Two parts. First, figure out *why* the debt exists. Then, score *how bad* it's gotten. Do them in that order.

**Date:** [YYYY-MM-DD]
**Auditor:** [Name]
**Workflow or stack being looked at:** [e.g. "Outbound enrichment pipeline: Clay to Salesforce to Outreach"]

---

## Part 1: Why does this debt exist?

For anything you already know is messy in this workflow, ask two questions: did we choose this on purpose, or did it just happen? And was that a smart trade-off, or a shortcut we shouldn't have taken?

| What's messy | On purpose or by accident? | Smart trade-off or a shortcut? | What this means |
|---|---|---|---|
| [e.g. "No error handling on the enrichment webhook"] | On purpose | Shortcut | We knew this was risky and did it anyway to save time |
| [e.g. "Mapping logic only [Name] understands"] | By accident | Smart trade-off at the time | Nobody knew better yet — this happens to every team |

Quick way to think about it:
- **On purpose + smart trade-off** — "We're doing this fast now and will fix it later." Often fine, as long as "later" actually happens.
- **On purpose + shortcut** — "We didn't have time to do it properly." This is the kind that actually piles up and hurts you.
- **By accident + smart trade-off** — "We didn't know better yet, now we do." Totally normal, happens to everyone.
- **By accident + shortcut** — Nobody even realized this was a problem. Usually means a training gap, not someone's fault.

## Part 2: How bad is it?

Score each one from 1 (healthy) to 5 (bad). Takes about 10 minutes.

| # | What to look at | Ask yourself | Score |
|---|---|---|---|
| 1 | Documentation | If the owner quit tomorrow, could someone else run this from what's written down? | [ ] |
| 2 | Who owns it | Is there one clear owner, or does everyone assume someone else is watching it? | [ ] |
| 3 | How fragile it is | How many things (one login, one person, one automation) would break the whole thing if they went away? | [ ] |
| 4 | Manual patch-ups | How much of this "automated" workflow is actually someone quietly fixing it by hand? | [ ] |
| 5 | How long to learn | How long would it take a new hire to understand this well enough to safely change it? | [ ] |
| 6 | How well tools talk to each other | Are the tools connected cleanly, or is there duct tape (manual exports, copy-pasting between systems)? | [ ] |
| 7 | Data quality | Do you trust this data, or does someone quietly not trust the numbers? | [ ] |
| 8 | Room to grow | Would this break if volume doubled next quarter? | [ ] |

**Total:** [ ] out of 40

## What the score means

| Score | Status | What it means |
|---|---|---|
| 8-14 | 🟢 Solid | Working and understood. Minor cleanup at most. |
| 15-22 | 🟡 Shaky | Works, but there are cracks. Fix it before it gets worse. |
| 23-30 | 🟠 Held together with tape | Actively slowing the team down. Make this a priority. |
| 31-40 | 🔴 One bad day away from breaking | Treat this as urgent, not "someday." |

## What's actually driving the score

[Be specific. "The enrichment step depends on one person's personal login." "Nobody's touched this mapping logic since [name] left."]

## What to do next

- [ ] [Specific fix, e.g. "Write up how the Clay table works in a workflow doc"]
- [ ] Owner: [name]. Target date: [date]
- [ ] If this points to a real decision (fix it, replace it, or leave it alone), write that up in the Decision Log

---
*Run this again every few months on your important workflows, or whenever the person who owns something changes. Something that scored green six months ago can quietly turn red with no single big failure — that's exactly why it's worth checking again.*
