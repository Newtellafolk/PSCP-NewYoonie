"""MathforIT"""

import math as m
def mathforIT(rad):
    """math"""
    area = (m.pi * (rad**2))
    circum = ((2 * m.pi) * rad)
    print("Area: " "%.3f" %area)
    print("Circumference: " "%.3f" %circum)
    
mathforIT(float(input()))