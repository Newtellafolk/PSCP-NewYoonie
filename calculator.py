"""Calculator"""
def main():
    """calculator"""
    nnn = int(input())
    if nnn == 1:
        print(1)
    else:
        count = len(range(1, nnn + 1))
        round = count * 2
        print(round)

main()
