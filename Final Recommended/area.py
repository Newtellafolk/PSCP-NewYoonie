"""area"""

def area(line):
    'area check'
    keep = 0
    for _ in range(line):
        txt = input()
        txt = txt.replace(' ', '')
        keep += len(txt)
    print(keep)
area(int(input()))
