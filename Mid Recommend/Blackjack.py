"""Blackjack"""
def main():
    """score of card in hand"""
    my_card = int(input())
    score = 0
    kept = 0
    for i in range(my_card):
        i = i
        card = input()
        if card in "JQKjqk":
            score += 10
        elif card in "Aa":
            kept += 1
        else:
            score += int(card)
    while kept > 0:
        kept -= 1
        if score + 11 > 21:
            score += 1
        elif score == 10 and kept == 1:
            score += 1
        else:
            score += 11
    print(score)

main()
