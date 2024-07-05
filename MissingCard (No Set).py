"""MissingCard (No Set)"""
def main():
    """MissingCard (No Set)"""
    card = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    card_lst = []
    for i in card:
        card_lst.append(i+"S")
        card_lst.append(i+"H")
        card_lst.append(i+"D")
        card_lst.append(i+"C")
    for i in range(51):
        leftover = input()
        if leftover in card_lst:
            card_lst.remove(leftover)
    print(card_lst[0])
main()
