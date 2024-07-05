"""Elo"""
def main():
    """_"""
    get_ra = int(input())
    get_rb = int(input())
    choose = input()
    elo_a = 1 / (1 + 10**((get_rb - get_ra)/400))
    elo_b = 1 / (1 + 10**((get_ra - get_rb)/400))
    if choose == "A":
        print("%0.2f" %elo_a)
    elif choose == "B":
        print("%0.2f" %elo_b)
main()

