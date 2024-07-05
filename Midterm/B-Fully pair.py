"""B - Fully pair?"""
def main():
    """pair-pscp"""
    txt = input().lower()
    keep = ""
    kee = ""
    count = 0
    for check in txt:
        if keep.count(check) <= 0:
            keep += check
    for check in keep:
        if txt.count(check) % 2 != 0:
            kee += check
            count += 1
    if count == 0:
        print("fully paired")
    else:
        print(kee)
main()
