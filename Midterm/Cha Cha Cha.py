"""Cha Cha Cha"""
import math as m
def rage():
    """salary of hongbunjang"""
    result = 0
    work_day = int(input())
    for _ in range(1, work_day + 1):
        hour = m.ceil(float(input()))
        result += hour
    print(result * 8720)
rage()
