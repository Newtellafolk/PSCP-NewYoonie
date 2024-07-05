"""Difference"""
def main():
    """set"""
    num_a = int(input())
    num_b = int(input())
    set_a = set()
    set_b = set()
    for _ in range(num_a):
        inset_a = int(input())
        set_a.add(inset_a)

    for _ in range(num_b):
        inset_b = int(input())
        set_b.add(inset_b)

    keep = set_a - set_b
    result = sorted(keep)
    for i in result:
        print(i, end=' ')
main()