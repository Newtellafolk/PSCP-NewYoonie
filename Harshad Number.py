"""Harshad Number"""
def main():
    """_"""
    for _ in range(10):
        num = int(input())
        if num == 0:
            print("No")
        elif len(str(num)) == 1:
            if num % num == 0:
                print("Yes")
            else:
                print("No")
        else:
            if num % result(num) == 0:
                print("Yes")
            else:
                print("No")

def result(num):
    """sum"""
    suum = 0
    if num < 0:
        for i in str(num)[1:]:
            suum += int(i)
        suum *= -1
    else:
        for i in str(num):
            suum += int(i)
    return suum

main()
