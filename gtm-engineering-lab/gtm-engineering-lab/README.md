# GTM Engineering Lab

A public, evolving library for people who want to learn AI, sales, and GTM engineering **by building**, not by reading threads and bookmarking them forever.

This isn't a one-time content drop. It's a working repo that grows weekly, built in the open, with templates, prompts, workflows, and code that anyone can use, fork, or improve. If you're the kind of person who learns by shipping something small every day, this is your library.

## What this is

- A collection of ready-to-use templates, scripts, and patterns for GTM/RevOps engineering
- A running log of what's been built, what broke, and what was learned
- A place to contribute your own work and get feedback from other builders
- Not a course, not a paid product, not a "drop and disappear" repo

## How it's organized

| Folder | What's in it |
|---|---|
| [`technical-debt/`](./technical-debt) | Templates and scorecards for auditing GTM systems — decision logs, mistake logs, debt scorecards, workflow docs |
| [`cold-email/`](./cold-email) | Copy, sequences, deliverability guides, and scripts |
| [`prompting/`](./prompting) | Prompt libraries and patterns organized by use case |
| [`automation-workflows/`](./automation-workflows) | Clay, n8n, Zapier, and Make recipes for GTM automation |
| [`ai-agents/`](./ai-agents) | Agent design patterns and example builds |
| [`sql/`](./sql) | GTM/RevOps queries and schema examples |
| [`community/`](./community) | Weekly update log, contributor list, public wins/fails log |
| [`resources/`](./resources) | Curated external tools, reading, and reference links |

Each top-level folder has its own README explaining what belongs there and what "good" looks like.

## How to contribute

Short version: fork it, add your thing following the naming convention, open a PR. Full details, quality bar, and template usage are in [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## Naming convention

- Folders and files: lowercase, kebab-case (`cold-email-sequence-saas-trial.md`, not `ColdEmailSequenceSaaSTrial.md`)
- Templates live in a `templates/` subfolder inside their category; filled-in examples live in `examples/`
- Dated entries (logs, weekly updates) use `YYYY-MM-DD` prefixes, e.g. `2026-07-15-mistake-log-clay-enrichment.md`

## Weekly update log

Every week, something new gets added — a template, a workflow, a prompt set, or a real example from a live build. The running log lives in [`community/weekly-updates.md`](./community/weekly-updates.md). Star/watch the repo if you want to follow along, or check that file weekly.

## License

Everything here is free to use, fork, and adapt. Attribution appreciated, not required. (Swap in whatever license, MIT recommended for max reuse — before you publish.)
