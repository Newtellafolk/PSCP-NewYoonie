"""Nearer"""
def main():
    """_"""
    alice_x = int(input())
    bob_x = int(input())
    itim_x = int(input())
    pikad_a = abs(itim_x - alice_x)
    pikad_b = abs(itim_x - bob_x)
    if pikad_a > pikad_b:
        print("Bob", pikad_b)
    elif pikad_b > pikad_a:
        print("Alice", pikad_a)
    elif pikad_a == pikad_b:
        print("Sundaes", pikad_a)
main()
