"""SequenceXXX"""
def main():
    """pattern"""
    num1 = int(input())
    num2 = int(input())
    for i in range(num1):
        for k in range(num2):
            for j in range(num1):
                if i == j or i == 0 or j == 0 or i == num1-1\
or j == num1-1 or i+j == num1-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            if k != num2:
                print(" ", end="")
        print()
main()
