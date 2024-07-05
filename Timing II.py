"""Timing II"""


def timetimetime():
    """_"""
    sec = int(input())
    minutes = sec // 60
    seconds = sec % 60
    hours = minutes // 60
    minutes = minutes % 60
    days = hours // 24
    hours = hours % 24
    if sec >= 0 and sec < 24 * 60 * 60:
        print("%04d" %days, "%02d" %hours, "%02d" %minutes\
, "%02d" %seconds, sep=":", end=" ")
    else:
        print("ERR_:__:__:__")
timetimetime()
