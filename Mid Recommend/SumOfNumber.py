"""SumOfNumber"""
def sumsum():
    """SumOfNumber"""
    num_total = int(input())
    keep = 0
    while True:
        num = int(input())
        keep += num
        if num == -1:
            keep += 1
            break
        elif keep == num_total:
            break
        # num = int(input())
        # if num == -1:
        #     break
        # keep += num
        # if keep == num_total:
        #     break
    print(keep)

sumsum()
