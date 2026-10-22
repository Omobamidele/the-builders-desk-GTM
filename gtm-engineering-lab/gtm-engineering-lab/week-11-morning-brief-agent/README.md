# Week 11 — Build Your Own Morning Brief Agent

Anthropic recently announced Claude Duet, a proactive assistant that watches your email, calendar and Slack, tells you what needs attention, and asks before it does anything. Right now it's waitlist-only.

You don't have to wait. This folder is a do-it-yourself version you can run today with n8n (a no-code automation tool) and a Claude API key. It's simpler than the real product, but it does the core job: **every morning, one message that tells you what matters today, with draft replies ready for you to approve.**

## What it does, in plain English

Every morning at 8am, the agent:

1. Reads your unread email from the last 24 hours, tomorrow's calendar, and your Slack mentions.
2. Asks Claude: "Does this need me today?" for each item.
3. Prepares short notes and draft replies for the things that do.
4. Sends **you** one message (Slack DM or email to yourself) with everything sorted. That's it. It never replies to anyone on its own.

## The four steps

| Step | What happens | Where it lives |
|---|---|---|
| **1. Watch** | Pulls new items from Gmail, Google Calendar and Slack | The three "get" nodes in the n8n workflow |
| **2. Sort** | Claude puts each item in a bucket: needs you today, can wait, FYI, or ignore | `prompts/triage-prompt.md` |
| **3. Prepare** | For "needs you today" items, Claude writes a draft reply or a one-line prep note | `prompts/draft-reply-prompt.md` |
| **4. Ask** | You get one digest. You decide what to send, edit, or skip | The final "send digest to me" node |

## What you need

- An n8n account (n8n Cloud or self-hosted, either works)
- A Google account (Gmail + Google Calendar)
- A Slack workspace where you can add an app (optional, you can remove the Slack parts)
- A Claude API key from the Anthropic Console (usage is billed by Anthropic; check their current pricing)
- About an hour for the first setup

Not technical? Follow [`SETUP-CHECKLIST.md`](./SETUP-CHECKLIST.md) step by step.

## The safety rule

**Nothing sends without your approval.** The workflow only ever sends one message, and it goes to you. Drafts are text in your digest. You copy, edit and send them yourself. If you later add auto-sending, you've changed the deal: test heavily first, and keep a human check on anything that goes to a customer.

Also:
- Claude only sees what the workflow passes it. Keep the lookback window short (24h) so you're not sending more than you need.
- If your company has rules about sending email content to AI tools, check them first.

## Try it with no real inbox

The `sample-data/` folder has fictional emails, meetings and Slack mentions from made-up companies. Paste them into the triage prompt in any Claude chat to see how sorting works before you connect anything real.

## How to customise

- **Change the time:** edit the "Every day 8am" schedule node.
- **Change what counts as urgent:** edit the "What counts as needs-you-today" list in `prompts/triage-prompt.md`. Add your own VIP names, key accounts, or keywords.
- **Change your voice:** add 2–3 of your real past replies as examples in `prompts/draft-reply-prompt.md`.
- **Email instead of Slack:** the workflow includes both "send to me" nodes; disable the one you don't want.
- **Add sources:** any n8n node that outputs text (HubSpot, Notion, Linear, etc.) can feed into the Merge node.

## Files

```
week-11-morning-brief-agent/
├── README.md
├── SETUP-CHECKLIST.md
├── prompts/
│   ├── triage-prompt.md
│   └── draft-reply-prompt.md
├── n8n/
│   └── morning-brief-workflow.json
└── sample-data/
    ├── sample-emails.json
    ├── sample-meetings.json
    ├── README.md
    └── sample-slack-mentions.json
```
