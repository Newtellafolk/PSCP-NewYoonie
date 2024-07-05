"""Sequence I"""
def main(num):
    """sequence I"""
    for _ in range(1, num + 1):
        for col in range(1, num + 1):
            print(col, end=" ")
        print()
main(int(input()))