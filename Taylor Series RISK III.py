#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 23:43:23 2024

@author: shaunspencer
"""

import numpy as np
import matplotlib.pyplot as plt

def taylor_exp(x):
    terms = [1, x, x*2/2, x*3/6]
    return sum(terms)

x_values = np.linspace(-0.5, 0.5, 500)
y_values = [taylor_exp(x) for x in x_values]

plt.plot(x_values, y_values, label='Taylor Series (n=4)')
plt.plot(x_values, np.exp(x_values), label='exp(x)')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Taylor Series Approximation of exp(x)')
plt.show()