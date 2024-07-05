"""Saitama"""
import math as m
def main():
    """how many day to achieve your goal"""
    vit_round = int(input())
    situp_round = int(input())
    looknang_round = int(input())
    runn_km = int(input())
    d_vit = int(input())
    d_sit = int(input())
    d_run = int(input())
    d_looknang = int(input())
    vit = vit_round/d_vit
    situp = situp_round/d_sit
    run = runn_km/d_run
    looknang = looknang_round/d_looknang
    if vit > situp:
        wan1 = vit
    else:
        wan1 = situp
    if looknang > run:
        wan2 = looknang
    else:
        wan2 = run
    if wan1 > wan2:
        print(m.ceil(wan1))
    else:
        print(m.ceil(wan2))
main()
