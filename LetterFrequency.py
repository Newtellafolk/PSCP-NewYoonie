"""LetterFrequency"""
def main():
    """LetterFrequency"""
    txt = input()
    txt = txt.lower()

    countt = {}
    for char in txt:
        if char.isalpha():
            countt[char] = countt.get(char, 0) + 1
    most_letter = max(countt, key=countt.get)
    print(most_letter)
main()
