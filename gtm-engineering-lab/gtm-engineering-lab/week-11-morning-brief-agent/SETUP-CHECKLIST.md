# Setup checklist (no coding needed)

Tick each box as you go. If you get stuck, stop and test with the sample data first.

## Part 1 — Try it without connecting anything (10 min)
- [ ] Open a chat with Claude.
- [ ] Paste everything in `prompts/triage-prompt.md` (below the `---` line).
- [ ] Paste the three files from `sample-data/` underneath.
- [ ] Check the result: does the sorting match what you'd do? If not, edit the "What counts as needs-you-today" list and try again.

## Part 2 — Get your accounts ready (15 min)
- [ ] Create or log in to n8n (n8n.io).
- [ ] Get a Claude API key: go to console.anthropic.com, add billing, create a key. Copy it somewhere safe. Never paste it into a shared doc.
- [ ] Decide where your digest goes: Slack DM to yourself, or email to yourself.

## Part 3 — Import the workflow (10 min)
- [ ] Download `n8n/morning-brief-workflow.json`.
- [ ] In n8n: **Workflows → Import from File** → choose the file.
- [ ] You'll see nodes with warning icons. That's normal: they need credentials.

## Part 4 — Connect credentials (15 min)
- [ ] Click **Get unread emails** → Credential → *Create new* → sign in with Google.
- [ ] Click **Get tomorrow's meetings** → connect Google Calendar → pick your calendar.
- [ ] Click **Get Slack mentions** → connect Slack. In the search query, replace `YOUR_SLACK_USER_ID` with your Slack member ID (Slack profile → ⋯ → Copy member ID). No Slack? Delete this node.
- [ ] Click **Ask Claude to triage** → Credential → *Create new* → **Header Auth**. Name: `x-api-key`. Value: your Claude API key.
- [ ] Click **Send digest to me (Slack)** → set the channel to your own user (a DM to yourself). OR enable **Send digest to me (email)** and set the To address to **your own** email.

## Part 5 — Test (10 min)
- [ ] Click **Execute workflow**.
- [ ] Check you received exactly one message, sent to you only.
- [ ] Read the drafts. Anything wrong or made up? Tighten the prompt.

## Part 6 — Turn it on
- [ ] Toggle the workflow to **Active**.
- [ ] Check your timezone under workflow **Settings** so 8am is your 8am.
- [ ] Review the digest daily for a week before trusting it.

## Safety check before going live
- [ ] The only "send" node goes to me.
- [ ] No node replies to emails or posts in shared channels.
- [ ] My API key is stored in n8n credentials, not typed into a node.
