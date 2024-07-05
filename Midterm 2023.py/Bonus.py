"""Bonus"""
def bonus():
    """_"""
    salary = int(input())
    years = int(input())
    month = int(input())
    if month >= 10:
        years += 1
    if years > 20:
        years = 20
    bonuss = salary * years
    if bonuss > 1000000:
        bonuss = 1000000
    if bonuss < 5000:
        bonuss = 5000
    print(bonuss)
bonus()

