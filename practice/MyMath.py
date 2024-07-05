"""MyMath"""

import math as m
def main():
    """_"""
    print(((m.sin(m.radians(90))) + (m.sin(m.radians(60))**2)) /\
((m.cos(m.radians(245**2))) + (m.cos(m.radians(180)))))
    print(((m.factorial(16)) * m.factorial(4)) / (m.factorial(8)))
    print((15 + 25) / ((25 - 12)**2 + (12 - 15)**2)**0.5)
    print(m.log(1234**4, 10))
    print((m.log(4234, 5) + m.log2(8191) + (71 * (m.log(156154, 10)))) /
(m.log(777, 7) - m.log(888, 8) - m.log(999, 9)))
main()