"""Fever"""
def main():
    """fever check"""
    temp = float(input())
    if temp >= 40.0:
        print("Very High Fever")
    elif 39.0 <= temp < 40:
        print("High Fever")
    elif 38.0 <= temp < 39.0:
        print("Mild Fever")
    elif 36.0 <= temp < 38.0:
        print("No Fever")
main()
