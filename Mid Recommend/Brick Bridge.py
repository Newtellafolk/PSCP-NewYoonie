"""Brick Bridge"""
def main():
    """_"""
    small = int(input())
    large = int(input())
    goal = int(input())
    if small * 1 + large * 5 < goal or large % 5 > small:
        print(-1)
    else:
        if large * 5 >= goal:   #ถ้าก้อนใหญ่สร้าได้พอดี or เหลือ
            print(goal % 5)
        else:                   #ถ้าก้อนใหญ่น้อยกว่า
            print(goal-(large*5))
main()
