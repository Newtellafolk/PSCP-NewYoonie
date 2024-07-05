"""Password"""
import math as m
def main():
    """Password Strength"""
    string1 = input()
    for length in range(1, len(string1)+1):
        print(length)
    entro = (m.log2(26**9))
    print(m.floor(entro))
main()
