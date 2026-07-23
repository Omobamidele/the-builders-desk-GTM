# GTM Mistake Log: [Short Description]

The point of this file isn't to catch someone doing something wrong. It's so the same mistake doesn't cost the team twice.

One rule that matters more than the rest: assume whoever was involved had good intentions and did the best they could with what they knew at the time. The real question is never "who broke it," it's "what let this happen, and what are we changing so it can't happen the same way again." If this file doesn't end with a specific fix and an owner, it might as well not exist.

**Date:** [YYYY-MM-DD]
**Logged by:** [Name]
**Category:** Cold Email / Automation / Data or Enrichment / AI Agent / SQL or Reporting / Process / Other
**Severity:** Low / Medium / High / Critical

---

## What happened

One or two plain sentences. No blame, just facts. [e.g. "An enrichment tool pushed 4,000 unverified emails into an active sequence. Bounce rate spiked to 11% and our sending domain got paused."]

## What it cost us

| Type | Detail |
|---|---|
| Cost ($) | [If you can put a number on it] |
| Time lost | [Hours or days] |
| Pipeline / deals affected | [Number or description] |
| Deliverability / reputation hit | [If it applies] |

## How we found out

[Did an alert catch it? Did a person notice? Did a customer complain? This tells you whether you need better detection, not just a better fix.]

## What happened, in order

| Time | Event |
|---|---|
| [Time or date] | [What happened] |
| | |

## Why it actually happened

Keep asking "why" until you hit something about the system, not a person. This is called the Five Whys — it's an old trick from Toyota's factories, and it works just as well here.

1. Why did [the mistake] happen? → [answer]
2. Why did that happen? → [answer]
3. Why did that happen? → [answer]
4. Why did that happen? → [answer]
5. Why did that happen? → [this last one is usually the real thing worth fixing]

## What made this possible

Usually more than one thing has to line up for a mistake like this to happen. List them here, focused on the system, not the person.

- [e.g. "Nothing checked email quality before it hit the sequence"]
- [e.g. "The bounce rate alert was set too high to catch it early"]

## What actually went right

[What limited the damage, or caught it faster than it could've been caught. Worth writing down too, not just the bad part.]

## What we're changing

| Fix | Type | Owner | Due |
|---|---|---|---|
| [Specific, checkable fix] | Fixes this one instance | | |
| [Specific, checkable fix] | Fixes the whole category of problem | | |

## Related decision log entry

[Link it here if this led to a real process or tool change]

---
*If you're reading this before you were about to do the same thing, good. That's the whole point.*
