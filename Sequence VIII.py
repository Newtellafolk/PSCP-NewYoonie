"""Sequence VIII"""
def sequence(num):
    """_"""
    for i in range(num):
        print("   " * (num - i - 1), end='')
        for j in range(i+1):
            if j == i:
                print("%02d" %(j + 1))
            else:
                print("%02d" %(j + 1), end=" ")

sequence(int(input()))
