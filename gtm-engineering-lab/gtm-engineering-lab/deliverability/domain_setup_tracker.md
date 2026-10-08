# 📋 Domain Setup Tracker

Fill one row per sending inbox. Copy it into a sheet if you prefer. Re-check DNS whenever you change sending tools.

Status key: ✅ passing · ❌ failing · ⏳ not checked yet

| Domain | Inbox | SPF | DKIM | DMARC (policy) | Aligned? | Tracking domain / off | Warmup start date | Current daily volume | Notes |
|---|---|---|---|---|---|---|---|---|---|
| example-outreach.com | name@example-outreach.com | ⏳ | ⏳ | ⏳ (p=none) | ⏳ | off | YYYY-MM-DD | 0 | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |

## Per-domain checks

| Domain | MX resolves (CheckMX) | On a blocklist? (MXToolbox) | In Postmaster Tools? | Spam rate this week | Bounce rate this week |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |

## Free tools for each column

- SPF: https://mxtoolbox.com/spf.aspx
- DKIM: https://mxtoolbox.com/dkim.aspx (you need your DKIM selector)
- DMARC: https://mxtoolbox.com/dmarc.aspx
- MX / setup: https://toolbox.googleapps.com/apps/checkmx/
- Blocklists: https://mxtoolbox.com/blacklists.aspx
- Spam rate: https://postmaster.google.com (Google asks for under 0.3%, ideally under 0.1%)
