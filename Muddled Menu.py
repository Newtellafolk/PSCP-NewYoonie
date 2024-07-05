"""Muddled Menu"""
def main():
    """Muddled Menu"""
    list1 = []
    while True:
        info = input()
        if info == "DONE":
            break
        elif info == "CLOSED":
            list1 = []
            return print("Full Course: " + str(list1) + " Reversed: " + str(list1))
        elif info[0:10] == "Can't do: ":
            list1.remove(info[10:])
        elif info == "SOMETHING'S WRONG":
            list1.clear()
            continue
        else:
            info = info.split(" #")
            if info[1].isnumeric():
                list1.insert(int(info[1]) - 1, info[0])
            else:
                list1.append(info[0])
    print("Full Course: " + str(list1) + " Reversed: " + str(list1[::-1]))

main()
