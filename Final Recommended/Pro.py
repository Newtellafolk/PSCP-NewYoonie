"""Pro"""
def main():
    """Pro"""
    come = int(input())
    pay = int(input())
    price_pers = int(input())
    comejing = int(input())
    pro = (comejing//come)*pay
    notpro = comejing % come
    cal_pro = pro * price_pers
    cal_notpro = notpro * price_pers
    total_pay = cal_pro + cal_notpro
    print(total_pay)
 
main()