"""Turnstile"""
def main():
    """check people"""
    unlocked = 0
    people = 0
    while True:
        txt = input().upper()
        if txt == "END":
            break
        elif txt == "C":
            unlocked = 1
        elif txt == "P" and unlocked:
            people += 1
            unlocked = 0
    print(people)
main()
