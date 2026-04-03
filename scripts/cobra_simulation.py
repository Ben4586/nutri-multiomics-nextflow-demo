import cobra
from cobra.io import load_model
import pandas as pd

model = load_model("textbook")

solution = model.optimize()

fluxes = solution.fluxes.reset_index()
fluxes.columns = ["reaction", "flux"]

fluxes.to_csv("cobra_fluxes.csv", index=False)