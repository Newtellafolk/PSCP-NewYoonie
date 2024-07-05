"""timing"""


def timetime():
    """timing"""
    sec = int(input())
    minutes = sec // 60
    seconds = sec % 60
    hours = minutes // 60
    minutes = minutes % 60
    days = hours // 24
    hours = hours % 24
    print(days, hours, minutes, seconds)

timetime()
