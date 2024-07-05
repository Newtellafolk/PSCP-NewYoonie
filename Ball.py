"""BALL"""
def dengdeng():
    """ball deng"""
    high = float(input())
    deng = 0
    while high >= 0.01:
        high = (high/5*3)
        deng += 1
    print(deng - 1)
dengdeng()
