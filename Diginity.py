"""Diginity"""
def main():
    """cal"""
    while True:
        num_card = input()
        if num_card == "0":
            break
        while len(num_card) > 1:
            num_card = str(sum([int(laek) for laek in num_card]))
        print(num_card)
main()
