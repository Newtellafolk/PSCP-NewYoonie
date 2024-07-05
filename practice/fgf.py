"""align"""
def main():
    """_"""
size = int(input())
alignment = input().lower()
text = input()

if alignment == "center":
    total_space = size - len(text)
    left_space = total_space // 2
    right_space = total_space - left_space
elif alignment == "right":
    left_space = size - len(text)
    right_space = 0
else:
    left_space = 0
    right_space = size - len(text)

if left_space < 0:
    print("ข้อความยาวเกินไปสำหรับขนาดที่กำหนด")
else:
    sign = " " * left_space + text + " " * right_space
    print(sign)

main()
