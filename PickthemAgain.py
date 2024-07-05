"""PickthemAgain"""
def main():
    """_"""
    laek = input().split()
    list1 = []
    list2 = []
    for newlaek in reversed(laek):
        list1.append(newlaek)
    for ans in list1:
        if int(ans) % 3 == 0 or int(ans) % 5 == 0:
            list2.append(ans)
    if list2 == []:
        print("Nope")
    else:
        for result in list2:
            print(result)

main()
