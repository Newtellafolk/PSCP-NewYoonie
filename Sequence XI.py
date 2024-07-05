"""Sequence XI"""
def main():
    """_"""
    num = int(input())
    for i in range(num * 2 - 1):
        iii = (num - abs(num - i - 1)) - 1
        for j in range(num * 2 - 1):
            jjj = num - abs(j - num + 1)
            if j == num * 2 - 2:
                print("%02d" %(jjj if jjj <= iii else iii + 1))
            else:
                print("%02d" %(jjj if jjj <= iii else iii + 1), end=" ")
main()
