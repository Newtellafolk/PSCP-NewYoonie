"""BTU"""
def main():
    """BTU"""
    result = 0
    area = int(input())
    height = int(input())
    people = int(input())
    room = input()
    sun = input()
    keep1 = add(area)
    if 100 <= area <= 2500:
        if height > 8:
            btu_add1 = (height - 8)*1000
            result = keep1 + btu_add1
        else:
            result += keep1
        if people > 2:
            btu_add2 = (people - 2)*600
            result += btu_add2
        else:
            result += 0
        if room == "Normal":
            result += 0
        else:
            result += 4000
        if sun == "facing the sun":
            result = (result*110)//100
        elif sun == "shaded":
            result = (result*90)//100
        else:
            result += 0
    print(result)

def table1(area):
    """suitable1"""
    if 100 <= area <= 150:
        return 5000
    elif 151 <= area <= 250:
        return 6000
    elif 251 <= area <= 300:
        return 7000
    elif 301 <= area <= 350:
        return 8000
    elif 351 <= area <= 400:
        return 9000
    elif 401 <= area <= 450:
        return 10000
    elif 451 <= area <= 550:
        return 12000

def table2(area):
    """suitable2"""
    if 551 <= area <= 700:
        return 14000
    elif 701 <= area <= 1000:
        return 18000
    elif 1001 <= area <= 1200:
        return 21000
    elif 1201 <= area <= 1400:
        return 23000
    elif 1401 <= area <= 1500:
        return 24000
    elif 1501 <= area <= 2000:
        return 30000
    elif 2001 <= area <= 2500:
        return 34000

def add(area):
    """usethis"""
    if area < 551:
        return table1(area)
    else:
        return table2(area)

main()
