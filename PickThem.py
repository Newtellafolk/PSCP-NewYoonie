"""PickThem"""
import json as j
def main():
    """odd"""
    num = input()
    keep = j.loads(num)
    list1 = []
    for index in keep:
        if index % 2 == 0 or index == 0:
            list1.append(index)
    if list1 == []:
        print("Nope")
    else:
        for result in list1:
            print(result)

main()

