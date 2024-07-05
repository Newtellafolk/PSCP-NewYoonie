"""FOR!F-Ball"""
def main():
    """where is a ball"""
    txt = input()
    posi = 1
    if len(txt) <= 1000:
        for i in txt:
            if i == "A":
                if posi == 1:
                    posi = 2
                elif posi == 2:
                    posi = 1
            elif i == "B":
                if posi == 2:
                    posi = 3
                elif posi == 3:
                    posi = 2
            elif i == "C":
                if posi == 3:
                    posi = 1
                elif posi == 1:
                    posi = 3
        print(posi)
main()
