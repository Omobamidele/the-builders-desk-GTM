"""Counts skills across the 100 LinkedIn postings in /workspace/gtm-job-market/postings.json.
Method: case-insensitive regex on title + description; a posting counts once per skill if the term appears anywhere.
Presence of a keyword is a demand signal, not proof the skill is required."""
import json,re,csv,collections
import sys
d=json.load(open(sys.argv[1] if len(sys.argv)>1 else '/workspace/gtm-job-market/postings.json'))
T=lambda p:(p['title']+'\n'+p['description'])
R={
 'CRM (HubSpot or Salesforce)':r'hubspot|salesforce',
 'Salesforce':r'salesforce',
 'HubSpot':r'hubspot',
 'APIs':r'\bapis?\b',
 'SQL':r'\bsql\b',
 'Python':r'\bpython\b',
 'Python, JavaScript/TypeScript or Node':r'\bpython\b|javascript|typescript|node\.?js',
 'LLMs / AI (OpenAI, Claude, GPT, LLM)':r'\bllms?\b|openai|claude|\bgpt|anthropic',
 'Clay':r'\bclay\b',
 'n8n':r'\bn8n\b',
 'Zapier':r'zapier',
 'Workato':r'workato',
 'Any of Clay, n8n, Zapier or Workato':r'\bclay\b|\bn8n\b|zapier|workato',
 'Enrichment':r'enrich',
 'Lead/account scoring':r'(lead|account|icp|fit)\s+scor|scoring',
 'Lead routing / assignment':r'routing|round[- ]robin|lead assignment|assignment rules',
 'Enrich or score or route':r'enrich|scoring|\bscore|routing|round[- ]robin|lead assignment',
 'Outbound / prospecting / sequences (exact words)':r'outbound|prospecting|cold email|sequenc',
 'Sales Ops / Sales Operations named':r'sales ops|sales operations',
 'Reporting / dashboards / forecasting':r'dashboard|reporting|forecast',
 'CRM data hygiene':r'data hygiene|data quality|dedup|de-dup|clean(ing)? up|data integrity',
 'Measured results (ROI, A/B test, experiment, measurable/pipeline/revenue impact)':r'\broi\b|a/b test|experiment|measurable impact|pipeline impact|revenue impact',
 'Remote word in title/location/description':r'\bremote\b',
}
res=[]
for k,r in R.items():
    c=sum(bool(re.search(r,T(p),re.I)) for p in d)
    by={cat:sum(bool(re.search(r,T(p),re.I)) for p in d if p['role_category']==cat) for cat in ['GTM Engineer','RevOps / Revenue Operations Engineer','Growth Engineer / Outbound Engineer']}
    res.append((k,c,by))
cats=collections.Counter(p['role_category'] for p in d)
for k,c,by in sorted(res,key=lambda x:-x[1]): print(f'{c:3d}  {k}  {list(by.values())}')
nocode=sum(not re.search(r'\bpython\b|javascript|typescript|node\.?js|\bsql\b',T(p),re.I) for p in d)
print('no python/js/sql mention:',nocode)
crm_out=sum(bool(re.search(r'hubspot|salesforce',T(p),re.I)) and bool(re.search(r'outbound|prospecting|sequenc|cold email',T(p),re.I)) for p in d)
print('crm AND outbound',crm_out)
sdr=sum(bool(re.search(r'\bsdr\b|\bbdr\b|sales development|business development|account executive|\bAEs?\b',T(p),re.I)) for p in d)
print('mentions sdr/bdr/ae terms',sdr)
print(cats)
with open('skills-from-100-postings.csv','w',newline='') as f:
    w=csv.writer(f);w.writerow(['skill_or_task','postings_out_of_100','GTM_Engineer_of_45','RevOps_of_35','Growth_Outbound_of_20','match_pattern'])
    for k,c,by in sorted(res,key=lambda x:-x[1]):
        if k.startswith('Remote'): continue
        w.writerow([k,c,*by.values(),R[k]])

nocode=[p for p in d if not re.search(r'\bpython\b|javascript|typescript|node\.?js|\bsql\b',T(p),re.I)]
print('NO_CODE',len(nocode))
