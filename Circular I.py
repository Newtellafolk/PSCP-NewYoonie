"""Circular I"""
def mosquito():
    """_"""
    center_x = float(input())
    center_y = float(input())
    rad = float(input())
    mos_pikad_x = float(input())
    mos_pikad_y = float(input())
    distance = (((mos_pikad_x - center_x)**2) + ((mos_pikad_y -center_y)**2)) ** 0.5
    if rad >= distance:
        print("Yes")
    else:
        print("No")

mosquito()
