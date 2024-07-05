"""Binary"""
def main():
    """Binary"""
    leak = int(input())
    keep = ''
    if leak == 0:
        print(0)
    while leak > 0:
        if leak % 2 == 0:
            keep += '0'
        else:
            keep += '1'
        leak //= 2
    print(keep[::-1])

main()
