"""BloodDonation"""
def main():
    """BloodDonation"""
    age = int(input())
    weight = int(input())
    roundd = int(input())
    if age < 17 or age > 70 or weight < 45:
        print("No")
    else:
        if age == 17 or 60 <= age <= 70 and weight >= 45:
            have_bai = input()
            if have_bai == "True":
                if roundd == 0 and age <= 55:
                    print("Yes")
                elif roundd > 0:
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
        else:
            if roundd == 0 and 56 <= age <= 59:
                print("No")
            else:
                print("Yes")

main()
