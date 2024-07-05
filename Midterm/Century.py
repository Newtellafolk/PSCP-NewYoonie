"""Century"""
import math as m
def main():
    """century"""
    laek = int(input())
    for _ in range(laek):
        year = input()
        if year.count("B.E.") == True:
            x_1 = year.strip("B.E. ")
            new_y = int(x_1) - 543
            if new_y < 0:
                print("ERROR")
            else:
                print(m.ceil((int(x_1) - 543)/100))
        elif year.count("A.D. ") == True:
            x_1 = year.strip("A.D. ")
            print(m.ceil(int(x_1)/100))
        else:
            print("ERROR")
main()
