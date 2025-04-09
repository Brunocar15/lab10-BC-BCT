import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b): 
    return a + b

def subtract(a, b): 
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b): 
    if a == 0:
        raise ValueError
    return b / a   

def logarithm(a, b): 
    if a ==0:
        raise ValueError
    if b<=0 or b==1:
        raise ValueError
    return math.log(a, b)

def exponent(a, b):
    math.pow(a, b)  





