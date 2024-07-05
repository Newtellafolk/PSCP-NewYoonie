"""seeker"""
def main():
    """seeker"""
    txt = input()
    keep = ''
    result = 0
    for i in txt:
        if i.isdigit():
            keep += i
        else:
            if keep == '':
                result += 0
            else:
                result += int(keep)
                keep = ''
    if keep.isdigit():
        print(result + int(keep))
    else:
        print(result)
main()
