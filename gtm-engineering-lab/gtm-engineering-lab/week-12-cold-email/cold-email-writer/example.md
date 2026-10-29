# Worked example: sequence-writer

> **Fictional example.** Every company, person, domain and number below is made up to show the format. Acme Analytics, Brightpath Logistics, Northwind Dental and similar names are not real customers or results. `.example` domains are reserved and never resolve.

## Scenario
Acme Analytics (fictional) writes a sequence for shop owners hiring an ads manager.

## Before (what the user gives)

```text
Persona: shop owner
Signal: hiring first paid ads manager
Offer: see which ads make profit
```

## After (what the skill should produce)

```text
Email 1 (day 1)
Subject: your new ads hire / ads that pay
Hi Priya, saw Fernleaf is hiring its first paid ads manager. The first thing a new ads hire usually gets asked is which ads actually make money after product costs. Would a short note on how other shops check that be useful?

Email 2 (day 4)
Subject: a 3-line profit check
A quick way to check one ad: ad spend, orders from that ad, product cost per order. If the first is bigger than the other two combined, it's losing money. Happy to share the sheet.

Email 3 (day 9), different angle: time spent copying numbers into spreadsheets.
Email 4 (day 15), close the loop: "Shall I stop here?"

A/B: Email 1 subject B = "question about Fernleaf's ads"
Run compliance-check before sending.
```

## Why this is a good result
Leads with the signal, gives value in email 2, no fake Re:, no invented results.
