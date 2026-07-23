# Decision Log: [Short Decision Title]

> **Format note:** This is adapted from the Architecture Decision Record (ADR) format Michael Nygard defined in 2011 for software teams, extended with the "decision drivers / options considered" structure from MADR (Markdown Any Decision Records). Software teams use this to make sure a decision is never a mystery to the next person — this repo applies the same discipline to GTM tooling, process, and workflow decisions, which almost nobody documents this rigorously.

**Decision ID:** DL-[###]
**Title:** [One line — name the decision, not the topic. "Move outbound sequencing from Outreach to Smartlead" not "Sequencing tool"]
**Date:** [YYYY-MM-DD]
**Owner:** [Name / role — the person accountable for this decision]
**Status:** `Proposed` → `Accepted` → `Deprecated` / `Superseded`
*(Once a decision is Accepted, don't edit it — if it changes later, open a new entry with Status "Supersedes DL-###" and link back. The log stays an honest history, not a wiki.)*
**Review date:** [YYYY-MM-DD — when this should be revisited, especially for anything time-boxed or "temporary"]

---

## Context and problem statement

What's the situation forcing a decision? What breaks, or what opportunity is on the table, if nothing changes?

[2-4 sentences. Be concrete: what wasn't working, what triggered this, what's the actual question being answered.]

## Decision drivers

The factors that actually matter for this call — not a generic list, the real constraints.

- [e.g. Budget ceiling]
- [e.g. Time to implement before a launch]
- [e.g. Team's existing skill set / tool familiarity]
- [e.g. Data portability / lock-in risk]

## Options considered

| Option | Pros | Cons |
|---|---|---|
| **A: [name]** | | |
| **B: [name]** | | |
| **C: [often "do nothing / stay as-is"]** | | |

## Decision outcome

**Chosen option:** [Option X]

**Why:** [The reasoning that actually tipped it — reference back to the decision drivers above. If two options scored similarly, say what broke the tie.]

## Consequences

**Positive**
- [What gets easier or better because of this]

**Negative / trade-offs accepted**
- [What gets harder, what risk is now live, what we're consciously giving up]

## Who's affected

[Teams, workflows, or tools that touch this decision]

## Related

- Related Workflow Doc: [link]
- Related Mistake Log entry (if this decision followed a failure): [link]
- Ticket / Slack thread / doc: [link]

---
*The Decision Log is append-only. Superseding a decision doesn't erase it — it shows the org learning in public.*
