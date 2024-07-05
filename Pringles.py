"""Pringes"""
def main():
    """_"""
    kob1 = input()
    chips = input()
    kob2 = input()
    fing_size = int(input())
    can_eat = chips[:fing_size]
    have_chips = chips[fing_size:]
    count = 0
    keep = 0
    for i in can_eat:
        if i == ")":
            count += 1
    for i in have_chips:
        if i == ")":
            keep += 1
    print(count)
    if keep == 0:
        print("None.")
    else:
        print("There are still some left.")
    print(kob1)
    print(" "*fing_size+have_chips)
    print(kob2)
main()
