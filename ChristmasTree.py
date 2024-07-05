"""ChristmasTree"""
def tree():
    """christmas tree"""
    wide = int(input())
    height = int(input())
    for i in range(1, wide + 1):
        print(" " * (wide - i), end="")
        print("*" * (2 * i - 1))
    for i in range(height):
        print(" " * (wide - 2) + "---")

tree()
