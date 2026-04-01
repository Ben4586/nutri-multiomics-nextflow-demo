import pandas as pd
import matplotlib.pyplot as plt

# Load integrated data
df = pd.read_csv("results/integrated.csv")

# Remove non-feature columns
df = df.drop(columns=["sample_id"])

# Compute correlation
corr = df.corr()

plt.figure()
plt.imshow(corr)
plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Correlation Heatmap (Multi-Omics)")
plt.tight_layout()

plt.savefig("results/correlation_heatmap.png")
plt.show()