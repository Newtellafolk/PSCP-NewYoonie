"""Run Length Encoding"""
def main():
    """brief"""
    txt = input() + " "
    count = 1
    keep = ""
    for i in range(1, len(txt)):
        if txt[i] == txt[i - 1]:
            count += 1
        else:
            keep += str(count) + txt[i - 1]
            count = 1
    print(keep)
main()
