"""Home Run"""
def main():
    """Hom run"""
    num_n = int(input())
    looktok = float(input())
    home_run = 0
    for _ in range(1, num_n + 1):
        lenght = float(input())
        if looktok > lenght:
            home_run += 1
    print(home_run)
main()
