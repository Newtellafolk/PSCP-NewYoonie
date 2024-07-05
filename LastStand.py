"""LastStand"""
def main():
    """_"""
    num = input().strip('[]').split(',')
    for i in num:
        print(i[-1])

main()
