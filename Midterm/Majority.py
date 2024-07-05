"""Majority"""
def main():
    """Majority"""
    count_lead = int(input())
    keep = []
    score = []
    for _  in range(int(input())):
        voter = input()
        keep.append(voter)
    for i in range(1, count_lead + 1):
        score.append([i, keep.count(str(i))])
        half = len(keep) / 2
        peek = max(score, key=lambda x: x[1])
    if peek[1] > half:
        print(*peek)
    else:
        print(0, peek[1])
main()
