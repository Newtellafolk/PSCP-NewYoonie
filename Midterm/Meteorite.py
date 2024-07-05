"""Meteorite"""
def main():
    """Meteorite"""
    weight = float(input())
    break_b = int(input())
    size_c = float(input())
    shot = 1
    meteo = 0
    while weight >= size_c:
        meteo += shot
        shot = break_b*shot
        weight /= break_b
    print(meteo)

main()
