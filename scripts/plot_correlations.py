import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("results/integrated.csv")

# Keep only numeric columns
df_numeric = df.select_dtypes(include=["number"])

# Compute correlation with glucose
corr = df_numeric.corr()["glucose"].drop("glucose").sort_values()

# Plot
plt.figure()
plt.barh(corr.index, corr.values)
plt.xlabel("Correlation with Glucose")
plt.title("Causal Feature Relationships")

plt.tight_layout()
plt.savefig("results/causal_correlations.png")
plt.show()