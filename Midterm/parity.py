"""Parity"""
def main():
    """parity"""
    bits = input()
    txt = input()
    trans = bits.replace("0", "")
    if txt == "Even":
        if len(trans) % 2 == 0:
            print(bits+"0")
        else:
            print(bits+"1")
    if txt == "Odd":
        if len(trans) % 2 == 0:
            print(bits+"1")
        else:
            print(bits+"0")

main()
