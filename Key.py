"""KEY"""
def keykey():
    """print ค่า Key"""
    id_card = input()
    key1 = 0
    for i in range(len(id_card)):
        key1 += int(id_card[i])
    key2 = int(id_card[-3:]) * 10
    sumsum = key1 + key2
    if sumsum < 1000:
        sumsum += 1000
    print(str(sumsum)[-4:])

keykey()
