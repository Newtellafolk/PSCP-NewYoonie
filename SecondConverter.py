"""SecondConverter"""
def main():
    """different time"""
    time_k = int(input())
    time_s = int(input())
    time_m = int(input())
    time_h = int(input())
    sec = time_k % time_s
    minute = time_k // time_s
    hour = minute // time_m
    minute = minute % time_m
    hour = hour % time_h
    if hour > time_h:
        hour = hour % time_h
    print("%d:%d:%d" %(hour, minute, sec))
main()
