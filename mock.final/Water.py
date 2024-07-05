"""Water"""
def main():
    """Water"""
    month_n = int(input())
    baht_a = float(input())
    max_b = float(input())
    over_c = float(input())
    max_baht_d = float(input())
    keep = 0
    for _ in range(month_n):
        water_use = float(input())
        if water_use <= max_b:
            tmp = water_use * baht_a
        else:
            tmp = ((water_use - max_b)*over_c) + (max_b * baht_a)
        if tmp <= max_baht_d:
            keep += 0
        else:
            keep += tmp
    print("%0.2f" %keep)

main()
