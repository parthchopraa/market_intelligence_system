import pandas as pd
from pathlib import Path

path = Path("Data/processed/asset_risk_summary.csv")
df = pd.read_csv(path)

df["risk_score"] = df["annual_volatility"] * 100

df.to_csv(path, index=False)
print("Added risk_score column")
print(df.head())
