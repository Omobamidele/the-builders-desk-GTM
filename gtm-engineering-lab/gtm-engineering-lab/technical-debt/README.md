# Technical Debt / GTM Systems Auditing

Four templates that work together as one system, not four separate documents. This is the same operating pattern mature software engineering teams use — Architecture Decision Records, runbooks, blameless postmortems, and tracked technical debt — applied to GTM/RevOps tooling, which almost nobody documents this rigorously yet.

| Template | Answers | Borrowed from |
|---|---|---|
| **Decision Log** | Why did we build/choose it this way? | Michael Nygard's ADR format (2011) + MADR |
| **Workflow Doc** | What does it do, and why does it exist? | Runbook practice, "why not just how" |
| **Mistake Log** | What broke, and what are we changing? | Google SRE's blameless postmortem + Five Whys |
| **Debt Scorecard** | How much hidden complexity is in here right now? | Martin Fowler's Technical Debt Quadrant (2009) |

**How they connect:** a Decision Log entry explains why a workflow was built a certain way → the Workflow Doc documents what it does day-to-day and links back to that decision → if it breaks, the Mistake Log captures what happened and links back to the workflow → the Scorecard periodically audits the whole thing and flags when it's time to open a new Decision Log entry. Used together, you get a real audit trail instead of four disconnected documents nobody reads twice.

- `templates/` — the four blank templates, ready to copy and fill in
- `examples/` — real filled-in examples from actual audits (contribute yours here)

Start with the Debt Scorecard on one workflow you already suspect is fragile. It'll tell you which of the other three templates to reach for next.
