"""Phone Number"""
def main():
    """Domestic or International"""
    phone_num = input()
    txt = input()
    if txt == "Domestic":
        if len(phone_num) == 9:
            print(phone_num[:1], phone_num[1:5], phone_num[5:9])
        else:
            print(phone_num[:2], phone_num[2:6], phone_num[6:10])
    elif txt == "International":
        if len(phone_num) == 9:
            print("+66" + phone_num[2:0], phone_num[-8:-4], phone_num[-4:])
        else:
            print("+66" + phone_num[1:2], phone_num[-8:-4], phone_num[-4:])

main()
