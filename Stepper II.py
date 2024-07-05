"""Stepper II"""
def main(num_m, num_n):
    """_"""
    if num_m > num_n:
        for i in range(num_m, num_n + 1, 1):
            print(i)
    else:
        for i in range(num_m, num_n - 1, -1):
            print(i)
main(int(input()), int(input()))
