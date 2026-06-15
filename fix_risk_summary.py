import pandas as pd
from pathlib import Path

base = Path("Data/processed")
df = pd.read_csv(base / "market_features.csv")

asset_col = "asset" if "asset" in df.columns else "symbol" if "symbol" in df.columns else "ticker"
ret_col = "daily_return" if "daily_return" in df.columns else "return" if "return" in df.columns else "log_return"

risk = df.groupby(asset_col).agg(
    annual_return=(ret_col, lambda x: x.mean() * 252),
    annual_volatility=(ret_col, lambda x: x.std() * (252 ** 0.5)),
    max_drawdown=(ret_col, "min")
).reset_index()

risk = risk.rename(columns={asset_col: "asset"})
risk["sharpe_ratio"] = risk["annual_return"] / risk["annual_volatility"]
risk["risk_category"] = pd.cut(
    risk["annual_volatility"],
    bins=[-1, 0.2, 0.5, 999],
    labels=["Low", "Medium", "High"]
)
risk["market_stance"] = risk["sharpe_ratio"].apply(
    lambda x: "Bullish" if x > 1 else "Neutral" if x > 0 else "Bearish"
)

risk.to_csv(base / "asset_risk_summary.csv", index=False)
print("Fixed asset_risk_summary.csv")
print(risk.head())
