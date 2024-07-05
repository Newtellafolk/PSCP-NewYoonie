"""Heads and Legs"""
def main():
    """Heads and Legs"""
    total_head = int(input())
    total_legs = int(input())
    rab, leftover = divmod(total_legs - 2 * total_head, 2)
    bird = total_head - rab
    if bird >= 0 and rab >= 0 and leftover == 0:
        print(rab, bird)
    else:
        print("Impossible")
main()
