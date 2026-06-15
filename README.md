# QuantEdge Intelligence Terminal

# Integrated Portfolio Optimization and Investment Forecasting Platform

A comprehensive financial analytics platform that combines market data engineering, forecasting, portfolio optimization, risk analytics, and interactive visualization to support data-driven investment decisions.

Developed as a Capstone Project for the Master of Data Analytics program at the University of Niagara Falls Canada.

# Overview

QuantEdge Intelligence Terminal is an end-to-end market intelligence system designed to help investors evaluate financial assets, optimize portfolio allocations, and identify investment opportunities across stocks and cryptocurrencies.

The platform integrates historical and real-time market data with quantitative analytics to generate actionable investment insights through a centralized dashboard.


# Business Problem

Financial markets generate large volumes of data, making it difficult for investors to simultaneously evaluate risk, forecast performance, optimize portfolios, and monitor market conditions.

This project addresses that challenge by providing a unified framework that combines:

* Market data collection
* Technical analysis
* Forecasting
* Risk assessment
* Portfolio optimization
* Backtesting
* Opportunity ranking


# Key Capabilities

# Market Data Integration

* Historical stock market data from Yahoo Finance
* Historical and live cryptocurrency data from Binance
* Real-time stock market data from Finnhub
* Automated data storage using SQLite

# Market Intelligence

* Technical indicator analysis (RSI, MACD, EMA, Bollinger Bands, ATR, VWAP)
* Buy, Hold, and Sell signal generation
* Market regime detection
* Asset-level opportunity scoring

# Forecasting & Risk Analytics

* ARIMA-based price forecasting
* Volatility analysis
* Sharpe Ratio calculation
* Maximum drawdown assessment
* Asset risk categorization

# Portfolio Optimization

* Maximum Sharpe Portfolio
* Minimum Volatility Portfolio
* Equal Weight Portfolio
* Correlation and diversification analysis

# Strategy Validation

* Historical backtesting
* Strategy vs. Buy-and-Hold comparison
* Win rate and risk-adjusted performance evaluation

# Interactive Dashboard

* Live Market Feed
* Asset Intelligence
* Portfolio Manager
* Opportunity Ranking
* Portfolio Optimization
* Correlation Analysis
* Backtesting Analytics


# Technology Stack

| Category         | Technologies                            |
| ---------------- | --------------------------------------- |
| Programming      | Python                                  |
| Data Processing  | Pandas, NumPy                           |
| Machine Learning | Scikit-learn                            |
| Forecasting      | Statsmodels (ARIMA)                     |
| Optimization     | SciPy                                   |
| Databases        | SQLite                                  |
| Visualization    | Plotly, Streamlit                       |
| Market Data      | Yahoo Finance, Binance API, Finnhub API |


# System Architecture

```text
Market Data Sources
(Yahoo Finance, Binance, Finnhub)
                │
                ▼
     Data Collection Layer
                │
                ▼
         SQLite Databases
                │
                ▼
      Feature Engineering
                │
                ▼
      Analytics Engine
   ├─ Forecasting
   ├─ Risk Analysis
   ├─ Market Regimes
   ├─ Correlation Analysis
   ├─ Portfolio Optimization
   └─ Backtesting
                │
                ▼
 Unified Market Intelligence
                │
                ▼
      Streamlit Dashboard
```


# Assets Analyzed

# Stocks

AAPL, MSFT, NVDA, TSLA, AMZN, GOOGL, META, JPM, V, SPY

# Cryptocurrencies

BTC, ETH, BNB, SOL, XRP

Dataset includes more than **35,000 historical market observations** collected from 2018 onward.


# Research Objectives

1. Compare the risk and return characteristics of stocks and cryptocurrencies.
2. Forecast short-term asset performance using historical market data.
3. Evaluate portfolio optimization strategies under different risk profiles.
4. Assess the impact of diversification on portfolio performance.
5. Develop an integrated investment recommendation framework.


# Key Results

* Maximum Sharpe Portfolio achieved the strongest risk-adjusted performance.
* Minimum Volatility Portfolio produced the lowest portfolio risk.
* Diversification across stocks and cryptocurrencies improved portfolio resilience.
* Opportunity ranking successfully identified high-potential investment candidates.
* Integrated analytics provided a unified framework for investment decision support.


# Running the Application

# Install Dependencies

```bash
pip install -r requirements.txt
```

# Launch Dashboard

```bash
streamlit run app.py
```
