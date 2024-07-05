"""OTP"""
def main():
    """OTP"""
    while True:
        rahut = input()
        if rahut == "0":
            break
        count_num = [rahut.count(str(i)) for i in range(10)]
        if len(rahut) == 4 and count_num.count(2) == 1:
            print("Valid")
        elif len(rahut) == 6 and (count_num.count(2) == 2 or count_num.count(3) == 1):
            print("Valid")
        elif len(rahut) == 8 and (count_num.count(2) == 3 or count_num.count(3) == 2):
            print("Valid")
        else:
            print("Invalid")
main()

