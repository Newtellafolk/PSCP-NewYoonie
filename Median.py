"""Median"""
def main():
    """median"""
    num = int(input())
    list1 = []
    for _ in range(num):
        laek = int(input())
        list1.append(laek)
        liang = sorted(list1)
    if  num % 2 == 1:
        print("%.1f" %liang[num//2])
    elif num % 2 == 0:
        cal = (liang[(num//2) - 1] + liang[num//2])/2
        print(cal)

main()
