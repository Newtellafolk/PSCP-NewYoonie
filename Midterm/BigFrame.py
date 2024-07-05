"""BigFrame"""
def main():
    """Frame"""
    txt1 = input().strip()
    txt2 = input().strip()
    txt3 = input().strip()
    txt4 = input().strip()
    txt5 = input().strip()
    max_length = max(len(txt1), len(txt2), len(txt3), len(txt4), len(txt5))
    up_down = "*"* (max_length + 4)
    print(up_down)
    print("* " + txt1 + ((max_length - len(txt1)) * " ") + " *")
    print("* " + txt2 + ((max_length - len(txt2)) * " ") + " *")
    print("* " + txt3 + ((max_length - len(txt3)) * " ") + " *")
    print("* " + txt4 + ((max_length - len(txt4)) * " ") + " *")
    print("* " + txt5 + ((max_length - len(txt5)) * " ") + " *")
    print(up_down)

main()
