"""Filter"""
import json as j
def main():
    """Filter"""
    dictt = j.loads(input())
    score = float(input())
    result = []
    for i in dictt:
        if dictt[i] >= score:
            result.append(i)
    if len(result) == 0:
        print("Nope")
    else:
        for i in sorted(result):
            print("%s\t%.2f" %(i, dictt[i]))
main()
