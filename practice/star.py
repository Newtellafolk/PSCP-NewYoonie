"""p"""
def main(star):
    """_"""
    for row in range(1, star + 1):
        for col in range(1, row + 1):
            print("* ", end="")
        print()
    for row in range(1, star + 1):
        for col in range(row, star + 1):
            print("* ", end="")
        print()
main(int(input()))