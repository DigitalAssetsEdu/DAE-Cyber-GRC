#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 19:45:42 2024

@author: shaunspencer
"""

import cgi  # Module for parsing URL parameters

def get_url_parameters():
    """Retrieves parameters from the URL."""
    form = cgi.FieldStorage()
    op1 = float(form.getvalue("op1", 0))  # Handle missing parameters gracefully
    op2 = float(form.getvalue("op2", 0))
    return op1, op2

def calculate_sum():
    """Calculates and prints the sum."""
    op1, op2 = get_url_parameters()
    sum = op1 + op2
    print("Content-Type: text/html")  # For web output
    print()  # Blank line after headers
    print(f"The sum is: {sum}")

if __name__ == "__main__":
    calculate_sum()
