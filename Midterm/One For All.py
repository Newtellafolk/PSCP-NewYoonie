"""One For All"""
def main():
    """gen"""
    num = int(input())
    word = ''
    for i in range(1, num + 1):
        if i == num:
            word += input() + "_"+ str(i)
        elif i % 2 == 0:
            word += input() + "-" * i
        else:
            word += input() + "*" * i
    print(word, end="")

main()
