"""AscendingSort"""
def main():
    """sort"""
    list1 = []
    for _ in range(5):
        num = int(input())
        list1.append(num)
        ascend = sorted(list1)
    for index in ascend:
        print(index)

main()
