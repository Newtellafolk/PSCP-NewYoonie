"""PH"""
def main():
    """PH"""
    num_ph = float(input())
    if 0 <= num_ph < 7:
        print("acidic")
    elif num_ph == 7:
        print("neutral")
    elif 7 < num_ph <= 14:
        print("akaline")
    else:
        print("error")
main()
