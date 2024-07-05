"""Left Arrow"""
def paifai():
    """left arrow"""
    wide = int(input())
    height = int(input())
    for i in range(height//2, 0, -1):
        print(" " * i + "*" * wide)
    for i in range((height//2) + 1):
        print(" " * i + "*" * wide)
paifai()
