"""Coke"""
def main():
    """coke"""
    price = int(input())
    fa_b = int(input())
    sale = int(input())
    want = int(input())
    cal = price * want
    if fa_b > 0 and want > 0:
        new_price = (want - 1) // fa_b
        cal -= new_price * (price - sale)
    print(cal)
main()
