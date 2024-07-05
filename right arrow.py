"""Right Arrow"""
def main():
    """paifai"""
    wide = int(input())
    height = int(input())
    for i in range(0, height//2, 1):
        print(" " * i + "*" * wide)
    for i in range(height//2, -1, -1):
        print(" " * i + "*" * wide)
main()
