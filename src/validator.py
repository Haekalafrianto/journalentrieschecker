import pandas as pd

# Load data

df = pd.read_excel("data/sample_entries.xlsx")
coa = pd.read_csv("data/chartofaccount.csv")

# Checkers

errors = []

if not df['Debit'].sum() == df['Credit'].sum():
    errors.append("Unbalanced Journal.")

invalid_account = df[~df['Account'].isin(coa)]
if not invalid_account.empty:
    errors.append(f"Invalid account found: \n {invalid_account['Account'].unique()}")

# Output

if errors:
    print("Validation failed")
    for e in errors:
        print("-", e)
else:
    print("All Checks Passed!")

