"""Backward"""
def back():
    """_"""
    word = []
    while True:
        txt = input()
        if txt == "NULL":
            break
        word.append(txt)
    for answer in reversed(word):
        print(answer)

back()