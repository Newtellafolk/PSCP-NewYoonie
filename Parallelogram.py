"""Parallelogram"""
def main():
    """parallelogram"""
    txt = input()
    for i in range(len(txt)):
        print(" " * (len(txt) - i -1) + txt[0:i + 1])
    for i in range(len(txt) - 1):
        print(txt[i+1:len(txt) + 1])
main()
