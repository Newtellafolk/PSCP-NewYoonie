"""3nPlus1"""
def main():
    """3nPlus1"""
    while True:
        result = 1
        num_n = int(input())
        if num_n == 0:
            break
        while num_n > 1:
            if num_n % 2 == 0:
                num_n //= 2
            else:
                num_n = (num_n * 3) + 1
            result += 1
        print(result)
main()
