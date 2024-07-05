"""Table I"""
def table():
    """x formular"""
    count = int(input())
    multi = 15
    for i in range(1, count + 1):
        result = multi * i
        print("15 x", i, "=", result)
    print()
table()
