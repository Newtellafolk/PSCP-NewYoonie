"""Helloooo"""
def main():
    """Helloooo"""
    txt = input()
    count = 0
    keep = ''
    vowels = ["a", "e", "i", "o", "u"]
    txt = txt[::-1]
    for i in txt:
        if i in vowels:
            count += 1
    for i in txt:
        if i in vowels and count != 0:
            keep += i*4
            count = 0
        else:
            keep += i
    txt = keep[::-1]
    print(txt)

main()
