import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import sys

df = pd.read_csv(sys.argv[1])

X = df.drop(columns=["sample_id", "glucose"])
y = df["glucose"]

model = RandomForestRegressor()
model.fit(X, y)

importance = pd.DataFrame({
    "feature": X.columns,
    "importance": model.feature_importances_
}).sort_values(by="importance", ascending=False)

importance.to_csv("feature_importance.csv", index=False)

joblib.dump(model, "model.pkl")