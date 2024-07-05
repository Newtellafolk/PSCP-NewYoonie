"""calculator"""
def calculator(num):
    """cal"""
    keep = 0
    for i in range(1, num + 1):
        if num == 1:
            keep += 1
            break
        else:
            keep += len(str(i))
    if keep == 1:
        print("1")
    else:
        print(num + keep)

calculator(int(input()))
