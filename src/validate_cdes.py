import pandas as pd
from datetime import datetime

# Step 1: Load data
data = pd.read_csv("../data/raw/cde_records.csv")

# Step 2: Check for missing or old data
data['missing_flag'] = data.isnull().any(axis=1)
data['freshness_days'] = (datetime.today() - pd.to_datetime(data['Last_Updated'])).dt.days

# Step 3: Filter invalid records
issues = data[(data['missing_flag']) | (data['freshness_days'] > 7)]

# Step 4: Export results
issues.to_excel("../data/processed/discrepancy_report.xlsx", index=False)
print("✅ Discrepancy report generated successfully!")
