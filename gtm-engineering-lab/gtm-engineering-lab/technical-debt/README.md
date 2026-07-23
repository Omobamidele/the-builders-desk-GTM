# Technical Debt / GTM Systems Auditing

Four templates that work as one system, not four separate things you fill out once and forget. Software teams already do this: they write down why they made a decision, document how things actually work, review what went wrong after a mistake, and keep an eye on how messy their systems are getting. This brings that same habit to GTM and RevOps tools, which almost nobody does yet.

| Template | What it answers |
|---|---|
| Decision Log | Why did we build or choose it this way? |
| Workflow Doc | What does it actually do, and why does it exist? |
| Mistake Log | What broke, and what are we changing? |
| Debt Scorecard | How messy has this gotten right now? |

How they fit together: a Decision Log entry explains why a workflow got built a certain way. The Workflow Doc explains what it does day to day and links back to that decision. If it breaks, the Mistake Log captures what happened and links back to the workflow. The Scorecard checks in on the whole thing every so often and flags when it's time to write a new Decision Log entry. Used together, you get a real trail you can actually follow later, not four documents nobody opens twice.

- `templates/` — the four blank templates, ready to copy and fill in
- `examples/` — real filled-in examples (add yours here)

Start with the Scorecard on one workflow you already suspect is messy. It'll point you toward which of the other three to use next.
