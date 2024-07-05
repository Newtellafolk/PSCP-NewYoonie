"""Diamond I"""
def main(deep, wide):
    """Diamond I"""
    dia = []
    value_dia = []
    for _ in range(deep):
        value = input().split()
        dia.append(value)
    for i in range(wide):
        cal = 0
        for j in dia:
            cal += int(j[i])
        value_dia.append(cal)
    print(max(value_dia))
main(int(input()), int(input()))
