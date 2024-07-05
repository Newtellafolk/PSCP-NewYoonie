"""Heron's formular"""
def main(aaa, bbb, ccc):
    """_"""
    sss = (aaa + bbb + ccc) / 2
    area = (sss * (sss - aaa) * (sss - bbb) * (sss - ccc))**0.5
    print("%0.3f" %area)

main(float(input()), float(input()), float(input()))
