"""CoinChangev1"""

def cal(change):
    """CoinChangev1"""
    coins = [25, 10, 5, 1]
    total = 0
    for coin in coins:
        total = total + change/coin
        change = change % coin
    return total

result = cal(int(input()))
print(result)
