"""Socks"""
def main():
    """Socks"""
    socks = input()
    socks = socks.upper()
    countt = {}
    for nub in socks:
        if nub.isalpha():
            countt[nub] = countt.get(nub, 1) + 1
    print(countt)
main()
