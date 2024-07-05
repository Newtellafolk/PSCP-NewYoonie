"""Align"""
def main():
    """align"""
    size = int(input())
    align = input().lower()
    txt = input()
    space_l = 0
    space_r = 0
    if align == "left":
        space_r = size - len(txt)
    elif align == "center":
        space_l = (size - len(txt)) // 2
        space_r = size - len(txt) - space_l
        if space_l != space_r:
            space_l += 1
    else:
        space_l = size - len(txt)
    result = " " * space_l + txt + " " * space_r
    print(result)
main()
