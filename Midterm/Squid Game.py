"""Squid Game"""
def main():
    """Tug-of-War"""
    force_a = 0
    force_b = 0
    for _ in range(10):
        team_a = int(input())
        force_a += team_a
    for _ in range(10, 20):
        team_b = int(input())
        force_b += team_b
    if force_a < force_b:
        print("A")
    elif force_a > force_b:
        print("B")
    else:
        print("AB")

main()
