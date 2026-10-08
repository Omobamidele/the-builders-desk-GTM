# ✈️ The Deliverability Pre-Flight Check

**Week 09 of The Builder's Desk. Free. No paywall, no email required.**

Most cold email problems aren't copy problems. The emails never reach the inbox, so nobody reads the copy.

And the usual order is backwards. People buy domains, write a sequence, load 2,000 leads, hit send, and only check DNS after replies dry up. By then the domain has a reputation, and it's not a good one.

This edition is the check you run *before* you scale. It splits into two kinds of items:

- **Required by inbox providers.** Google, Yahoo and Microsoft publish these. They're not opinions.
- **Best practice.** What cold email practitioners and sending tools commonly recommend. Useful, but they're norms, not rules, and I've labelled them that way.

Everything below is sourced, not invented. Links are at the bottom.

---

## First, what the providers actually require

Three mailbox providers have published sender rules. Here they are in plain English.

**Google (personal Gmail accounts).** Since February 1, 2024, *every* sender to Gmail needs SPF or DKIM, valid forward and reverse DNS (PTR) for sending IPs, a TLS connection, RFC 5322-formatted messages, and a spam rate in Postmaster Tools below 0.3%. If you send 5,000+ messages a day to Gmail, you also need SPF **and** DKIM, a DMARC record (p=none is fine), a From: domain aligned with SPF or DKIM, and one-click unsubscribe plus a visible unsubscribe link on marketing and subscribed messages. Google's FAQ says to keep spam rate below 0.1% and never let it reach 0.3%, that unsubscribes should be honored within 48 hours, and that enforcement ramped up from November 2025 with temporary and permanent rejections.

Two details people miss:
- Google counts the 5,000 across the **same primary domain**. 2,500 from `yourdomain.com` plus 2,500 from `mail.yourdomain.com` makes you a bulk sender.
- Google's FAQ says these guidelines apply to personal Gmail accounts, not Google Workspace accounts. Most B2B prospects are on Workspace or Microsoft 365. Treat the rules as the floor anyway. They're the only official, published version of what a mailbox provider expects.

**Yahoo.** All senders: SPF or DKIM, spam rate below 0.3%, valid forward and reverse DNS, RFC 5321/5322 compliance. Bulk senders: SPF **and** DKIM, DMARC at least p=none that passes, From: aligned with SPF or DKIM, one-click List-Unsubscribe for marketing and subscribed messages, a visible unsubscribe link, and unsubscribes honored within 2 days.

**Microsoft (Outlook.com, Hotmail, Live).** From May 5, 2025, domains sending more than 5,000 emails a day to Outlook.com consumer addresses must pass SPF and DKIM and publish DMARC at least p=none, aligned with SPF or DKIM (preferably both). Microsoft's April 29, 2025 update says non-compliant mail is rejected with `550; 5.7.515 Access denied`. Their Postmaster policy page describes junk-foldering first, then rejection if issues aren't fixed. Either way, it doesn't land.

The pattern across all three: **authenticate, align, make leaving easy, keep complaints low.** Everything else is a guess wearing a suit.

---

## The pre-flight, in 6 groups

### 1. Domain & DNS

Separate sending domains protect the domain your company actually runs on. Instantly's own setup guide recommends buying secondary domains for cold email "so we don't damage the reputation of your main domain." Yahoo also recommends segregating mail types by IP or DKIM domain.

Then authenticate every sending domain:
- **SPF** lists who may send for the domain. Keep it under 10 DNS lookups. RFC 7208 says evaluation past 10 returns a `permerror`.
- **DKIM** signs every message. Google requires 1024-bit or longer for personal Gmail and recommends 2048.
- **DMARC** at least `p=none`, ideally with a `rua` address so you actually get reports. Microsoft suggests moving gradually from none to quarantine to reject once legit sources are aligned.
- **Alignment.** The From: domain has to match the SPF or DKIM domain. This is the one that breaks when a tool sends "on behalf of" you without custom DKIM.
- **PTR and TLS.** If you send through Google Workspace or Microsoft 365, the provider handles these. If you run your own SMTP, you own them.

**The task:** run each sending domain through MXToolbox SPF, DKIM and DMARC lookups, and Google Admin Toolbox CheckMX. Fix anything red before moving on.

### 2. Inbox setup

Fewer inboxes per domain, real names, real reply addresses. Instantly's guide says max 3–5 accounts per domain. That's a vendor norm, not a provider rule. Microsoft recommends that From or Reply-To addresses are valid and can receive replies. Google's guidelines say display names should identify the sender, not carry subject lines or fake "Re:" threads.

**The task:** list every inbox, its domain, and confirm each one can receive a reply. Use the tracker template in this folder.

### 3. Warmup & volume

New inboxes need history before they carry campaign volume. Instantly says its done-for-you accounts need at least 2 weeks of warmup before campaigns. On daily caps, Instantly's guide says 30–50 emails per inbox per day, and Smartlead's 2026 guide says keep each mailbox at 50 or fewer, and under about 500 per domain. Again, vendor guidance.

Google's own guidelines say the same thing in a different voice: increase volume slowly, send at a consistent rate, avoid bursts, and don't suddenly double volume. If messages start bouncing or deferring, reduce volume until errors drop.

**The task:** divide your target daily volume by your inbox count. If the per-inbox number is over your cap, add inboxes or lower the target. The calculator in the tool does this.

### 4. List quality

Bounces tell providers you don't know who you're emailing. Verify every list before it goes into a sequence. Instantly's tracking checklist says to keep bounce rate under 2%, a line you'll see across most sending tools. Microsoft's hygiene recommendations say to remove invalid addresses regularly.

Be honest with yourself here too. Google's guidelines say don't buy lists and don't email people who didn't sign up. Cold outbound lives in tension with that. The practical answer is tight targeting, relevant reasons to reach out, and an easy way out.

**The task:** verify the list, remove anything invalid or risky, and make sure opt-outs are processed within 2 days.

### 5. Copy & links

Google requires one-click unsubscribe for *marketing and subscribed* messages from bulk senders. Whether a 1:1-style cold email counts as "marketing" is a grey area. A visible, simple opt-out is the safe default either way, and above 5,000/day to Gmail or Yahoo, add the one-click headers.

Tracking adds links and pixels. Instantly explains that without a custom tracking domain, your tracking links sit on a URL shared with other customers. Set up a custom tracking domain, or turn tracking off.

Google's formatting guidelines: links should be visible and easy to understand, don't hide content with HTML/CSS, and subject lines shouldn't start with "Re:" or "Fwd:" unless they really are.

**The task:** send your actual first email to mail-tester.com and read every line of the report, not just the score.

### 6. Monitoring

You can't keep spam rate under 0.3% if you never look at it. Set up Google Postmaster Tools for each sending domain. Watch the error codes Google and Microsoft return: `5.7.26` (authentication), `4.7.28` (rate limited, Google says pause at least 10 minutes), and `5.7.515` (Microsoft authentication). Check blocklists if you're on a shared IP.

**The task:** add every sending domain to Postmaster Tools today, and put a weekly check on your calendar.

---

## How to use the interactive tool

Open [`preflight.html`](./preflight.html). Download it and double-click. It runs offline, no sign-up, nothing leaves your browser.

1. Answer each item **Yes**, **No**, or **Not sure**. Each one tells you why it matters and links a free tool to check it.
2. Items tagged **Required by inbox providers** decide the verdict. Any "No" there means **Do not send yet**. Any "Not sure" means **Fix before scaling**.
3. Fill in the volume calculator: inboxes, target emails per day, and your per-inbox cap (defaults to 30, the low end of Instantly's 30–50 guideline, edit it to yours).
4. Read the prioritized fix list. Required items come first.
5. Hit **Copy my fix list** and paste it into your tracker or task board.

Your answers save in your browser. **Reset** clears them.

There's also [`domain_setup_tracker.md`](./domain_setup_tracker.md), a fill-in table for every domain and inbox you run.

Automate the sending. Keep the checking.

---

## Sources

**Provider requirements**
- Google, Email sender guidelines: https://support.google.com/a/answer/81126
- Google, Email sender guidelines FAQ (0.1% target, 48-hour unsubscribes, primary-domain counting, Workspace scope, November 2025 enforcement): https://support.google.com/a/answer/14229414
- Google, Sender requirements & Postmaster Tools FAQ: https://support.google.com/a/answer/14289100
- Google Postmaster Tools: https://postmaster.google.com
- Google, Set up Postmaster Tools: https://support.google.com/mail/answer/9981691
- Google Workspace, Set up SPF / DKIM / DMARC: https://support.google.com/a/answer/33786 · https://support.google.com/a/answer/174124 · https://support.google.com/a/answer/2466580
- Yahoo Sender Hub, Sender Best Practices: https://senders.yahooinc.com/best-practices/
- Yahoo Sender Hub, FAQs: https://senders.yahooinc.com/faqs/
- Yahoo Complaint Feedback Loop: https://senders.yahooinc.com/complaint-feedback-loop/
- Microsoft, Strengthening Email Ecosystem: Outlook's New Requirements for High-Volume Senders (Apr 2, 2025, updated Apr 29/30): https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%e2%80%99s-new-requirements-for-high%e2%80%90volume-senders/4399730
- Microsoft Outlook.com Postmaster: https://postmaster.outlook.com/ and policies: https://substrate.office.com/ip-domain-management-snds/postmaster/Policies
- RFC 7208 (SPF, 10-lookup limit): https://www.rfc-editor.org/rfc/rfc7208
- RFC 8058 (one-click unsubscribe): https://www.rfc-editor.org/rfc/rfc8058

**Practitioner guidance (vendor norms, not provider rules)**
- Instantly, Cold Email Strategy (secondary domains, 3–5 accounts per domain, 30–50/day, 2-week warmup): https://help.instantly.ai/en/articles/5975326-instantly-cold-email-strategy
- Instantly, Custom Tracking Domain: https://help.instantly.ai/en/articles/6984188-custom-tracking-domain-ctd
- Instantly, Email tracking implementation checklist (bounce rate under 2%): https://instantly.ai/blog/email-tracking-implementation-checklist-setup-onboarding-and-team-rollout-in-30-days/
- Smartlead, How many cold emails per day per domain (2026): https://www.smartlead.ai/blog/how-many-cold-emails-per-day
- Smartlead, Cold emails per day per mailbox benchmark: https://www.smartlead.ai/benchmarks/how-many-cold-emails-per-day-per-mailbox

**Free tools**
- MXToolbox SuperTool: https://mxtoolbox.com/SuperTool.aspx
- MXToolbox SPF / DKIM / DMARC / Blacklist checks: https://mxtoolbox.com/spf.aspx · https://mxtoolbox.com/dkim.aspx · https://mxtoolbox.com/dmarc.aspx · https://mxtoolbox.com/blacklists.aspx
- MXToolbox Email Health: https://mxtoolbox.com/emailhealth
- Google Admin Toolbox CheckMX: https://toolbox.googleapps.com/apps/checkmx/
- Google Admin Toolbox Dig (PTR lookups): https://toolbox.googleapps.com/apps/dig/
- mail-tester.com: https://www.mail-tester.com
- dmarcian DMARC Inspector (showed a maintenance notice when checked, MXToolbox DMARC is the backup): https://dmarcian.com/dmarc-inspector/
- Learn DMARC (visual walkthrough of SPF/DKIM/DMARC): https://www.learndmarc.com/
