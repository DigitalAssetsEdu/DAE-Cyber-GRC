#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 22:23:03 2024

@author: shaunspencer
"""

import yfinance as yf
import numpy as np
import pandas as pd
from scipy.stats import norm

class StockPortfolio:
    def __init__(self, tickers, shares, start_date, end_date):
        self.tickers = tickers
        self.shares = shares
        self.start_date = start_date
        self.end_date = end_date
        self.data = None

    def download_data(self):
        # Download historical data for all tickers
        data = yf.download(self.tickers, start=self.start_date, end=self.end_date)
        self.data = data['Adj Close']
        return self.data

    def compute_log_returns(self):
        # Compute daily logarithmic returns
        log_returns = np.log(self.data / self.data.shift(1)).dropna()
        return log_returns

    def compute_portfolio_var(self, log_returns):
        # Compute the variance-covariance matrix
        cov_matrix = log_returns.cov()
        # Calculate portfolio variance
        portfolio_variance = np.dot(self.shares, np.dot(cov_matrix, self.shares))
        return portfolio_variance

    def calculate_var(self, log_returns, confidence_level):
        # Calculate Value at Risk using the Delta-Normal method
        mean_log_return = np.dot(log_returns.mean(), self.shares)
        sd_portfolio = np.sqrt(self.compute_portfolio_var(log_returns))
        z_score = norm.ppf(1 - confidence_level)
        var_log_return = z_score * sd_portfolio - mean_log_return
        
        # Convert VaR to dollars
        initial_portfolio_value = np.dot(self.shares, self.data.iloc[-1])
        var_dollars = initial_portfolio_value * (np.exp(var_log_return) - 1)
        return var_dollars

# Example usage
tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'META', 'NVDA', 'TSLA']  # Example tickers
portfolio = StockPortfolio(tickers, [100]*7, '2020-01-01', '2023-12-31')
data = portfolio.download_data()
log_returns = portfolio.compute_log_returns()
var = portfolio.calculate_var(log_returns, 0.95)
print(f"The Value at Risk (VaR) at 95% confidence level is: ${var:.2f}")
