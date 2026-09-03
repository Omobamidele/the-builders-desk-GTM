"""
Lead Scoring Starter — Module 1 (Very Technical track), Week 6, Builder's Desk

A minimal, real starting point for scoring leads by ICP fit. This is not a
finished model — it's the scaffold the exercise asks you to build on top of.
Swap in your own dataset and adjust the weights to match your actual ICP
worksheet (see icp_worksheet.md in this same folder).

Requires: pandas, scikit-learn
    pip install pandas scikit-learn
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# ---------------------------------------------------------------------------
# 1. Load your data
# ---------------------------------------------------------------------------
# Expects a CSV with at least these columns. Replace with your own export
# from your CRM, or a public dataset while you're learning the pattern.
#
#   company_size      : int   (employee count)
#   industry_match    : int   (1 if industry matches your ICP, else 0)
#   tech_stack_match  : int   (1 if they use a tool that signals fit, else 0)
#   engagement_score  : int   (0-100, e.g. website visits, email opens)
#   converted         : int   (1 if they became a customer, 0 if not — this
#                               is what the model learns to predict)

DATA_PATH = "leads.csv"  # <-- point this at your real export

df = pd.read_csv(DATA_PATH)

feature_cols = ["company_size", "industry_match", "tech_stack_match", "engagement_score"]
X = df[feature_cols]
y = df["converted"]

# ---------------------------------------------------------------------------
# 2. Train a simple model
# ---------------------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# ---------------------------------------------------------------------------
# 3. Check it's actually learning something real
# ---------------------------------------------------------------------------
preds = model.predict(X_test)
print(classification_report(y_test, preds))

# ---------------------------------------------------------------------------
# 4. Score new, unconverted leads
# ---------------------------------------------------------------------------
# Replace this with your real pipeline of open/uncontacted leads.
new_leads = pd.read_csv("new_leads.csv")
new_leads["fit_score"] = model.predict_proba(new_leads[feature_cols])[:, 1]

ranked = new_leads.sort_values("fit_score", ascending=False)
print(ranked[["fit_score"] + feature_cols].head(20))

# Next step (part of the exercise, not this script):
# validate the top-ranked leads against your ICP worksheet by hand for a
# sample of 10-20 — a model that disagrees with your own judgment on
# obvious cases usually means a feature is missing, not that your
# judgment is wrong.
