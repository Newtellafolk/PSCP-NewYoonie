"""Run Length Decoding"""
def main():
    """_"""
    txt = input()
    result = ''
    keep = ''
    for i in txt:
        if i.isnumeric() == True:
            result += i
        if i.isalpha() == True:
            keep += int(result) * i
            result = ''
    print(keep)
main()
