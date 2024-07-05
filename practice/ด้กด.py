def main():
# อ่านขนาดของจอป้ายไฟ
    size = int(input())

    # อ่านคำสั่งให้ข้อความชิดซ้าย กึ่งกลาง หรือทางขวา
    alignment = input().strip()

    # อ่านข้อความ
    text = input().strip()

    # คำนวณช่องว่างทางซ้ายและทางขวา
    space_left = 0
    space_right = 0

    if alignment == "left":
        space_right = size - len(text)
    elif alignment == "center":
        space_left = (size - len(text)) // 2
        space_right = size - len(text) - space_left
    else:  # alignment == "right"
        space_left = size - len(text)

    # สร้างข้อความที่จะแสดงผล
    result = " " * space_left + text + " " * space_right

# แสดงผลลัพธ์
    print(result)
main()
