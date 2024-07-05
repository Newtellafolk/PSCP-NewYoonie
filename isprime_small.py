"""isprime_small"""
def main():
    """jamnuan chapor"""
    num = int(input())
    keep = "No"
    for i in range(1, num + 1):
        if num == 1 or num == 0:
            break
        if num % i == 0 and i != 1 and i != num:
            keep = "No"
            break
        else:
            keep = "Yes"
    print(keep)

main()
