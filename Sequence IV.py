"""Sequence IV"""
def main():
    """nub leak bab mai tummada"""
    num = int(input())
    for i in range(1, (num**2)+1):
        print(i, end=" ")
        if i % num == 0:
            print()
main()
