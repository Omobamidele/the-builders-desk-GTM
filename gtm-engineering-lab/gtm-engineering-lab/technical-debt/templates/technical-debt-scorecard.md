# Technical Debt Scorecard: [Workflow / Tool Stack Name]

> **Format note:** This scorecard works in two layers, both borrowed from software engineering practice and applied to GTM systems for probably the first time in a structured way. Layer 1 is Martin Fowler's Technical Debt Quadrant (2009) — it classifies *why* debt exists, along two axes: was it taken on deliberately or by accident, and was that choice prudent or reckless. Not all debt is bad — deliberate, prudent debt (shipping a scrappy version now, on purpose, to hit a deadline) is often the right call. Reckless debt, deliberate or not, is what actually slows teams down. Layer 2 is a numeric scoring rubric that tells you *how bad* it's gotten, banded against RevOps-style maturity stages. Classify first, then score — the quadrant tells you how urgently to care, the score tells you where to start.

**Date:** [YYYY-MM-DD]
**Auditor:** [Name]
**Workflow / stack being scored:** [e.g. "Outbound lead enrichment pipeline (Clay → Salesforce → Outreach)"]

---

## Layer 1: Classify the debt

For each piece of debt you already know about in this workflow, place it in a quadrant. This isn't scored — it's context for how to talk about it with the team.

| Debt item | Deliberate or Inadvertent? | Prudent or Reckless? | Quadrant | Notes |
|---|---|---|---|---|
| [e.g. "No error handling on the enrichment webhook"] | Deliberate | Reckless | *"We didn't have time for it"* | [Why it happened] |
| [e.g. "Mapping logic only [Name] understands"] | Inadvertent | Prudent | *"Now we know how we should've done it"* | [Why it happened] |

**The four quadrants, for reference:**
- **Deliberate + Prudent** — "We're shipping now and will deal with it later" — often a legitimate trade, if it actually gets revisited
- **Deliberate + Reckless** — "We don't have time to do this right" — the most dangerous kind; it compounds
- **Inadvertent + Prudent** — "Now we know how we should've done it" — normal, happens to every team as it learns
- **Inadvertent + Reckless** — nobody realized this was a problem — usually a training or process gap, not a person problem

## Layer 2: Score it

Score each dimension 1 (healthy) to 5 (critical). Takes 10-15 minutes.

| # | Dimension | Question to ask | Score (1-5) |
|---|---|---|---|
| 1 | **Documentation** | If the owner left tomorrow, could someone else run this from docs alone? | [ ] |
| 2 | **Ownership clarity** | Is there one clear owner, or does everyone assume someone else is watching it? | [ ] |
| 3 | **Fragility** | How many single points of failure (one API key, one person, one Zap) would break the whole thing? | [ ] |
| 4 | **Manual workarounds** | How much of this "automated" workflow actually depends on someone manually checking/fixing/exporting? | [ ] |
| 5 | **Onboarding time** | How long would it take a new hire to understand and safely modify this? | [ ] |
| 6 | **Integration health** | Are the tools talking to each other cleanly, or is there duct tape (manual CSV exports, copy-paste between systems)? | [ ] |
| 7 | **Data quality** | Does this workflow produce/rely on clean, trusted data, or does someone quietly not trust the numbers? | [ ] |
| 8 | **Scalability** | Does this break or need rework if volume doubles next quarter? | [ ] |

**Total score:** [ ] / 40

## Maturity band

| Range | Stage | Meaning |
|---|---|---|
| 8-14 | 🟢 **Defined** | Working, understood, low debt — minor cleanup at most |
| 15-22 | 🟡 **Emerging** | Functional but fragile in spots — schedule a fix before it compounds |
| 23-30 | 🟠 **Ad Hoc** | Duct-taped together, actively slowing the team — prioritize a rebuild |
| 31-40 | 🔴 **Critical** | One incident away from a real breakage — treat as urgent, not backlog |

## Specific red flags found

[List what's actually driving the score — e.g. "Enrichment step relies on a personal API key," "No one has touched the mapping logic since [name] left"]

## Recommended next action

- [ ] [Specific fix — e.g. "Document the Clay table logic in a Workflow Doc"]
- [ ] Owner: [name] — Target: [date]
- [ ] If this surfaces a real decision (rebuild vs. patch vs. leave it), log it in the Decision Log

---
*Re-run this scorecard quarterly on your core workflows, or any time something in the stack changes owners. A stack that scored 🟢 six months ago can quietly become 🔴 with zero single dramatic failure — that's the whole reason to keep re-scoring it.*
