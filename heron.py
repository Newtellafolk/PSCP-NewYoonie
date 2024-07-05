"""Heron's"""
def main():
    """heron"""
    put_a = float(input())
    put_b = float(input())
    put_c = float(input())
    if put_a > 0 and put_b > 0 and put_c > 0:
        sss = ((put_a + put_b + put_c) / 2)
        area = ((sss * (sss - put_a) * (sss - put_b) * (sss - put_c)) ** 0.5)
        print("%0.3f" %area)
main()
