"""Cardd"""
def main():
    """_"""
    card_type = input()
    lst = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
    if card_type[0] in lst:
        print(card_type[0] + " 0f ")
    elif card_type[0] == "A":
        print("Ace of")
main()
