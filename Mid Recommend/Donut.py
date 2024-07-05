"""Donut"""
def main(price, propiece, free, want):
    """donut"""
    buy = (propiece + free) * (want//(propiece + free))
    cost = (price * propiece) * (want//(propiece + free))
    if want - buy >= propiece:
        cost = cost + price * propiece
        buy = buy + (propiece + free)
    else:
        cost += price * (want - buy)
        buy = want
    print(cost, buy)

main(int(input()), int(input()), int(input()), int(input()))
