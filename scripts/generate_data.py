import numpy as np
import pandas as pd

np.random.seed(42)
n = 100

# Microbiome
species_A = np.random.rand(n)
species_B = np.random.rand(n)
species_C = 1 - (species_A + species_B)
species_C[species_C < 0] = 0

micro = pd.DataFrame({
    "sample_id": [f"S{i}" for i in range(n)],
    "species_A": species_A,
    "species_B": species_B,
    "species_C": species_C
})

# Metabolites
butyrate = species_A * 20 + np.random.normal(0, 2, n)
acetate = species_B * 30 + np.random.normal(0, 2, n)
propionate = species_C * 10 + np.random.normal(0, 1, n)

meta = pd.DataFrame({
    "sample_id": micro["sample_id"],
    "butyrate": butyrate,
    "acetate": acetate,
    "propionate": propionate
})

# Clinical outcome
glucose = 150 - butyrate*2 + acetate*1.5 + np.random.normal(0, 5, n)

clinical = pd.DataFrame({
    "sample_id": micro["sample_id"],
    "glucose": glucose
})

# Save
micro.to_csv("data/synthetic/microbiome.csv", index=False)
meta.to_csv("data/synthetic/metabolomics.csv", index=False)
clinical.to_csv("data/synthetic/clinical.csv", index=False)