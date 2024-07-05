"""Bad Keyboard"""
def keyboard():
    """edit"""
    txt = input()
    new_txt = ''
    for char in txt:
        if char == 'i':
            new_txt += 'o'
        elif char == 'o':
            new_txt += 'i'
        elif char == 'I':
            new_txt += 'O'
        elif char == 'O':
            new_txt += 'I'
        else:
            new_txt += char
    print(new_txt)

keyboard()
