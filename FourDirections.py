"""FourDirections"""
def main():
    """direction"""
    txt = input()
    if txt == "U":
        for i in range(2, 0, -1):
            print(" " * i + "*")