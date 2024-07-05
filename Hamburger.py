"""Hamburger"""
def hamburger():
    """_"""
    left_b = int(input())
    right_b = int(input())
    wide = (left_b + right_b) * 2
    print("|" * left_b + "*" * wide + "|" * right_b)
hamburger()
