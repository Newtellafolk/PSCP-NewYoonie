"""Tuple's Sad life"""
def main():
    """cool tuple's"""
    txt = input().split()
    choose = input()
    nub = txt.count(choose)
    index = txt.index(choose)
    for _ in range(nub):
        for _ in range(nub):
            print(str(index), end=" ")
        print()

main()
