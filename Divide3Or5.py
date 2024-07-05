"""Divide3Or5"""
def main():
    """divide"""
    num = float(input())
    kept = 0
    for i in range(1, int(num) + 1):
        if i % 3 == 0 or i % 5 == 0:
            kept += i
    print(kept)
main()
