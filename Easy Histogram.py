"""Easy Histogram"""
def main():
    """Easy Histogram"""
    txt = input()
    keep = {}
    for ch in txt:
        keep[ch] = keep.get(ch, 0) + 1
    sorted_keep = dict(sorted(keep.items(), key=lambda item: (item[0].lower(), item[0])))
    for alpha, nub in sorted_keep.items():
        print(f"{alpha} = {nub}")
main()
