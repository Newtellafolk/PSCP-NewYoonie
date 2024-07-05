"""Math for IT"""

import math as m
def main():
    """circle area"""
    rad = float(input())
    area = (m.pi * rad**2)
    circum =  (2 * m.pi * rad)
    print("Area: " "%0.3f" %area)
    print("Circumference: " "%0.3f" %circum)
main()
