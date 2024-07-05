"""Day I"""
def atikasuratin():
    """check"""
    christ = int(input())
    if christ >= 1 and christ % 4 == 0 and christ % 100 != 0 or christ % 400 == 0:
        print("Yes")
    else:
        print("No")

atikasuratin()
