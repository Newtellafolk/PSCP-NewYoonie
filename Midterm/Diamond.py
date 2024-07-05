"""Diamond"""
def main():
    """jearanai"""
    lenght = int(input())
    up_down = lenght // 2
    for i in range(lenght):
        for j in range(lenght):
            if i == up_down or i + j == up_down or i - j == up_down or \
                j == lenght - i + up_down - 1 or j - i == up_down:
                print("*", end="")
            else:
                print(" ", end="")
        print()

main()
