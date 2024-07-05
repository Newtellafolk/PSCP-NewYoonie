"""BootSequence"""
def boot():
    """_"""
    num = int(input())
    for i in range(1, num):
        print(i, end="_")
    print(num)

boot()
