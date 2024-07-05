"""Bill"""
def bill():
    """you have to pay"""
    food_brave = int(input())
    process = (10/100 * food_brave)
    if process <= 50:
        food_brave += 50
        vat = food_brave * 7/100
        summ = food_brave + vat
    elif process > 1000:
        food_brave += 1000
        vat = food_brave * 7/100
        summ = food_brave + vat
    else:
        vat = (food_brave + process) * 7/100
        summ = food_brave + process + vat
    print("%0.2f" %summ)

bill()
