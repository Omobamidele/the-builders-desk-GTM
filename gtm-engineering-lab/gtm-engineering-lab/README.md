# Week 09 — The Deliverability Pre-Flight Check

Most cold email problems aren't copy problems. The emails never reach the inbox. This week is the check to run before you scale any sending, split into what Google, Yahoo and Microsoft actually require and what practitioners recommend:

1. **Domain & DNS.** Separate sending domains, SPF, DKIM, DMARC (at least p=none), From: alignment, PTR and TLS.
2. **Inbox setup.** A few inboxes per domain, real sender names, replies that land somewhere.
3. **Warmup & volume.** Warm before you send, stay under a per-inbox cap, ramp slowly.
4. **List quality.** Verify before upload, keep bounces low, honor opt-outs within 2 days.
5. **Copy & links.** Easy opt-out, custom tracking domain or tracking off, few visible links.
6. **Monitoring.** Postmaster Tools on every domain, spam rate under 0.3% (aim under 0.1%), blocklists, bounce codes.

Every requirement is linked to the provider's own page. No paywall, no email required.

## Get the interactive version

Open [`deliverability/preflight.html`](./deliverability/preflight.html). Download it, double-click, and it runs offline. Answer yes / no / not sure for each item, and it gives you a verdict (**Clear to scale**, **Fix before scaling**, or **Do not send yet**), a prioritized fix list you can copy, and a per-inbox volume calculator.

The full lesson is in [`deliverability/README.md`](./deliverability/README.md), plus a fill-in [`domain_setup_tracker.md`](./deliverability/domain_setup_tracker.md).

## The free resources referenced

- Google Email sender guidelines: https://support.google.com/a/answer/81126
- Google Postmaster Tools: https://postmaster.google.com
- Yahoo Sender Best Practices: https://senders.yahooinc.com/best-practices/
- Microsoft Outlook high-volume sender requirements: https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%e2%80%99s-new-requirements-for-high%e2%80%90volume-senders/4399730
- MXToolbox SuperTool: https://mxtoolbox.com/SuperTool.aspx
- Google Admin Toolbox CheckMX: https://toolbox.googleapps.com/apps/checkmx/
- mail-tester.com: https://www.mail-tester.com
- dmarcian DMARC Inspector: https://dmarcian.com/dmarc-inspector/

## Previous edition

## Week 07 — The 30-Day Plan

I landed a GTM Engineering role in under 30 days. This is the exact structure I used, broken into the four things that actually get you hired:

1. **Your resume** — the bullet formula and the section order that gets you past the first skim.
2. **Your portfolio** — what to learn first (with real free resources), what to build with it, and how to write it up so it gets you hired.
3. **Getting in front of the right person** — the 3 real paths in (warm referral, direct outreach, applying with proof attached), not just cold email.
4. **Your interview answers** — a 4-part structure, worked examples, and a real bank of sourced GTM/RevOps interview questions to practice on.

### Get the interactive version

Everything above is built as a track-aware, interactive walkthrough (it asks where you sit technically and tailors the whole plan to that): [The 30-Day Plan](https://claude.ai/artifact/YUBYVUygK8UY26qUFWUxwM)

### The free resources referenced in the portfolio module

**Not technical (strategy, messaging, positioning)**
- [HubSpot Academy — Content Marketing Certification](https://academy.hubspot.com/courses/content-marketing) (free)
- [HubSpot Academy — Digital Marketing Certification](https://academy.hubspot.com/courses/digital-marketing) (free)

**Mid-technical (connecting tools)**
- [freeCodeCamp — APIs for Beginners](https://www.freecodecamp.org/news/apis-for-beginners/) (free)
- [Clay University — the HTTP API lesson](https://www.clay.com/university/lesson/http-api-clay-101) (free)

**Very technical (systems and data)**
- [SQLZoo — the JOIN tutorial](https://sqlzoo.net/wiki/The_JOIN_operation) (free)
- [Google BigQuery Sandbox](https://docs.cloud.google.com/bigquery/docs/sandbox) (free, no card required)

### Real interview questions to practice on

Sourced from published GTM/RevOps hiring guides ([Sloane Staffing](https://www.sloane-staffing.com/insights/gtm-engineer-interview-questions-job-description-template), [Fullcast](https://www.fullcast.com/content/revops-interview-questions/)) — the full, track-sorted bank with the practice tool is in the interactive plan above.
