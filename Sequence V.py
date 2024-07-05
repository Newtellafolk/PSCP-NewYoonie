"""Sequence V"""
def backward(num):
    """sequence"""
    count = 1
    for i in range(num, 0, -1):
        print(i, end=" ")
        if count % 7 == 0:
            print('')
        count += 1

backward(int(input()))
