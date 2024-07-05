"""Lift"""
def main():
    """lift"""
    people = int(input())
    lift_safe = float(input())
    dek = 0
    adult = 0
    w_keep = 0
    for _ in range(1, people + 1):
        age = int(input())
        weight = float(input())
        if age < 12:
            dek += 1
        else:
            adult += 1
        if weight > 0:
            w_keep += weight
    if adult == 0 and dek >= 1:
        print("Not Safe")
    elif w_keep > lift_safe:
        print("Not Safe")
    else:
        print("Safe")


main()
