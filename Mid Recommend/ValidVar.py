"""ValidVar"""
def main():
    """varld check"""
    num_var = int(input())
    w_restrict = "if else elif while for True False continue break\
 return is in and or from as pass not def None"
    harm = w_restrict.split(" ")
    for _ in range(1, num_var + 1):
        txt = input()
        if txt.isidentifier() == True and txt not in harm:
            print("Valid")
        else:
            print("Invalid")

main()
