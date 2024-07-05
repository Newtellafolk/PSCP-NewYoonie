"""ATM"""
def main():
    """ATM """
    keep_current = 0
    have = int(input())
    while True:
        d_or_w = input()
        if d_or_w == "END":
            break
        keep_current = history_list(d_or_w, have)
    print(keep_current)

def history_list(d_or_w, have):
    """transac"""
    yaek = d_or_w.split()
    if yaek[0] == "D":
        have += int(yaek[1])
    elif yaek[0] == "W":
        if have >= int(yaek[1]):
            have -= int(yaek[1])
        else:
            have -= have
    return have
main()
