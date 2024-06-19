#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 21:13:42 2024

@author: shaunspencer
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the stock prices range
stock_prices = np.arange(200, 401, 1)

# Define the strikes and premiums
strike_put_short = 285
strike_call_short = 350
strike_put_long = 280
strike_call_long = 350
premium_put_short = 2.55
premium_call_short = 5.86
premium_put_long = 11.17
premium_call_long = 21.30

# Payoff for short put
payoff_short_put = np.where(stock_prices < strike_put_short, strike_put_short - stock_prices, 0) - premium_put_short

# Payoff for short call
payoff_short_call = np.where(stock_prices > strike_call_short, stock_prices - strike_call_short, 0) - premium_call_short

# Payoff for long put
payoff_long_put = np.where(stock_prices < strike_put_long, strike_put_long - stock_prices, 0) - premium_put_long

# Payoff for long call
payoff_long_call = np.where(stock_prices > strike_call_long, stock_prices - strike_call_long, 0) - premium_call_long

# Total payoff
total_payoff = payoff_short_put + payoff_short_call + payoff_long_put + payoff_long_call

# Plotting the payoff diagram
plt.figure(figsize=(10, 6))
plt.plot(stock_prices, total_payoff, label='Total Payoff', color='blue')
plt.plot(stock_prices, payoff_short_put, '--', label='Short $285 Put (May 24)', color='red')
plt.plot(stock_prices, payoff_short_call, '--', label='Short $350 Call (May 24)', color='green')
plt.plot(stock_prices, payoff_long_put, '--', label='Long $280 Put (Sep 20)', color='orange')
plt.plot(stock_prices, payoff_long_call, '--', label='Long $350 Call (Sep 20)', color='purple')

# Add titles and labels
plt.title('Payoff Diagram for Strangle Strategy on Palo Alto Networks (PANW)')
plt.xlabel('Stock Price at Expiration')
plt.ylabel('Payoff')
plt.legend()
plt.grid(True)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(295.75, color='grey', linestyle='--')  # Mark the price after earnings announcement

# Show the plot
plt.show()
