import pandas as pd
from pathlib import Path

base = Path("Data/processed")
features = pd.read_csv(base / "market_features.csv")

asset_col = "symbol" if "symbol" in features.columns else "ticker" if "ticker" in features.columns else "asset"
ret_col = "daily_return" if "daily_return" in features.columns else "return" if "return" in features.columns else "log_return"

summary = features.groupby(asset_col).agg(
    avg_return=(ret_col, "mean"),
    volatility=(ret_col, "std")
).reset_index()

summary["risk_score"] = summary["volatility"].fillna(0) * 100
summary["risk_level"] = pd.cut(
    summary["risk_score"],
    bins=[-1, 2, 5, 1000],
    labels=["Low", "Medium", "High"]
)

summary.to_csv(base / "asset_risk_summary.csv", index=False)
print("Created Data/processed/asset_risk_summary.csv")
