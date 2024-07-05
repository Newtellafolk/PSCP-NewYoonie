"""PrasomSib"""
def main():
    """PrasomSib"""
    cal = 0
    result = 0
    laek = input()
    for i in range(len(laek) - 1):
        for j in range(len(laek)):
            cal = int(laek[i]) + int(laek[j])
            if cal == 10:
                result += 1
                break
            elif cal > 10:
                cal = int(laek[j])
    print(result)
main()
