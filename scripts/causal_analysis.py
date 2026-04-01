import pandas as pd

df = pd.read_csv("results/integrated.csv")

# Keep only numeric columns
df_numeric = df.select_dtypes(include=["number"])

# Compute correlation with glucose
corr = df_numeric.corr()["glucose"].sort_values()

print("=== Correlation with glucose ===")
print(corr)

# Save results
corr.to_csv("results/causal_correlations.csv")