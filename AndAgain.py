"""AndAgain"""
def main():
    """AndAgain"""
    txt = input().replace(".", "")
    keep = txt.split()
    word = []
    for i in keep:
        vowels = i.count("a") + i.count("e") + i.count("i") +\
 i.count("o") + i.count("u")
        if vowels >= 2:
            word.append(i)
    word.sort()
    if len(word) == 0:
        print("Nope")
    else:
        for ans in word:
            print(ans)

main()
