# GTM Mistake Log: [Short Description]

> **Format note:** This is adapted from Google SRE's blameless postmortem model and the Five Whys root-cause technique. The core rule, borrowed directly from that practice: assume everyone involved had good intentions and acted on the best information they had. The question is never "who broke it" — it's "what allowed it to break, and what are we changing about the system so it can't happen the same way twice." A mistake log entry without an owned, dated action item is indistinguishable from no entry at all — don't file this away without one.

**Date:** [YYYY-MM-DD]
**Logged by:** [Name]
**Category:** `Cold Email` / `Automation` / `Data / Enrichment` / `AI Agent` / `SQL / Reporting` / `Process` / `Other`
**Severity:** `Low` / `Medium` / `High` / `Critical`

---

## Summary

One or two sentences, plain language, no blame. [e.g. "A Clay enrichment waterfall pushed 4,000 unverified emails into an active sequence, spiking bounce rate to 11% and pausing sending domain-wide."]

## Impact

| Type | Detail |
|---|---|
| Cost ($) | [If quantifiable] |
| Time lost | [Hours/days] |
| Pipeline / deals affected | [Number or description] |
| Deliverability / reputation impact | [If applicable] |

## How it was caught

[Alert, a person noticing, a customer complaint, a scheduled review? This tells you whether you need better detection, not just a better fix.]

## Timeline

| Time | Event |
|---|---|
| [HH:MM or date] | [What happened] |
| | |

## Root cause — Five Whys

Keep asking "why" until you hit a system condition, not a person. Stop when the next "why" would just restate a policy ("because we don't have a QA step" is a real answer; "because someone rushed" usually isn't the end of the chain).

1. Why did [the mistake] happen? → [answer]
2. Why did *that* happen? → [answer]
3. Why did *that* happen? → [answer]
4. Why did *that* happen? → [answer]
5. Why did *that* happen? → [the systemic cause — this is usually the one worth fixing]

## Contributing factors

List everything that had to be true for this to happen — usually more than one thing. Framed at the system level, not the person level.

- [e.g. "No validation step between enrichment and sequence entry"]
- [e.g. "Alert threshold for bounce rate was set too high to catch it early"]

## What went well

[What limited the damage or caught it faster — worth reinforcing, not just what went wrong.]

## Action items

| Action | Type | Owner | Due date |
|---|---|---|---|
| [Specific, checkable fix] | Mitigative *(fixes this instance)* | | |
| [Specific, checkable fix] | Preventative *(fixes the class of problem)* | | |

## Related decision log entry

[Link to a Decision Log entry if this led to a formal process or tool change]

---
*If you're reading this before doing something similar — good, that's the whole point of this file existing.*
