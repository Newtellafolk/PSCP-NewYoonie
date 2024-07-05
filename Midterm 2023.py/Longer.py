"""Longer"""

import math as m
def main():
    """_"""
    rad = float(input())
    wide = float(input())
    long = float(input())
    circum = 2 * m.pi * rad
    rectang = (wide * 2) + (long * 2)
    dif1 = circum - rectang
    dif2 = rectang - circum
    if circum > rectang:
        print("Circle is longer")
        print("%0.5f" %dif1)
    elif rectang > circum:
        print("Rectangle is longer")
        print("%0.5f" %dif2)
    elif circum == rectang:
        print("Equal")
        print("%0.5f" %dif1)
main()
