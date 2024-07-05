"""All_Primes"""
def main(num):
    """All_Primes"""
    keep = 0
    for leak in range(1, num + 1):
        if is_prime(leak):
            keep += 1
    print(keep)

def is_prime(num):
    """prime"""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
main(int(input()))
