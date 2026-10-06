# Creates budget_data.csv: monthly budget and actual spend for 5 departments.
# Run with:  python generate_data.py
import numpy as np
import pandas as pd

np.random.seed(42)  # same data every time

# Monthly budget in 2023. Budgets grow 5% each year.
budgets = {"Engineering": 500000, "Sales": 200000, "Marketing": 150000,
           "Support": 120000, "Operations": 100000}

# Spending pattern by month (Jan-Dec): bonuses in March, quiet summer, holiday bump in December
seasonality = [1.0, 1.0, 1.15, 1.0, 1.0, 1.0, 0.9, 0.9, 1.0, 1.0, 1.0, 1.05]

# The 4 stories hidden in the data: (department, first month, last month, spending multiplier)
stories = [("Sales", "2023-01", "2026-12", 1.12),        # overspends every year
           ("Operations", "2024-06", "2024-07", 2.0),    # one-time office move
           ("Marketing", "2026-04", "2026-12", 1.35),    # campaign running over budget this year
           ("Support", "2026-01", "2026-12", 0.85)]      # hiring freeze this year

rows = []
for year in [2023, 2024, 2025, 2026]:
    for month_number in range(1, 13):
        month = f"{year}-{month_number:02d}"
        for dept in budgets:
            budget = round(budgets[dept] * 1.05 ** (year - 2023), -3)
            actual = budget * seasonality[month_number - 1] * np.random.normal(1, 0.03)
            for story_dept, start, end, multiplier in stories:
                if dept == story_dept and start <= month <= end:
                    actual = actual * multiplier
            if month > "2026-09":
                actual = None  # the future: not spent yet
            else:
                actual = round(actual)
            rows.append([month, dept, budget, actual])

df = pd.DataFrame(rows, columns=["month", "department", "budget", "actual"])

# 3 data problems to fix in the cleaning step
df = pd.concat([df, df.iloc[[100]]])                   # a duplicated row
df.loc[df.index[50], "actual"] = None                   # a missing actual
df.loc[df.index[132], "department"] = "Marketng"        # a misspelled department
df["budget"] = df["budget"].astype(int)
df["actual"] = df["actual"].astype("Int64")             # whole dollars, blanks allowed

df.to_csv("budget_data.csv", index=False)
print("Saved budget_data.csv with", len(df), "rows")
