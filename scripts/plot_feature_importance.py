import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/feature_importance.csv")

df = df.sort_values(by="importance")

plt.figure()
plt.barh(df["feature"], df["importance"])
plt.xlabel("Importance")
plt.title("Feature Importance")

plt.tight_layout()
plt.savefig("results/feature_importance.png")
plt.show()