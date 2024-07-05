"""Sequence III"""
def sequence():
    """sequence III"""
    num_n = int(input())
    for i in range(2, num_n + 2):
        for j in range(i, i + num_n):
            print(j, end=' ')
        print()
sequence()
