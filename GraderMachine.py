"""GraderMachine"""
def main():
    """gradermachine"""
    start_w = int(input())
    last_w = int(input())
    pass_p = ""
    total = 0
    if start_w <= last_w:
        for i in range(start_w, last_w + 1):
            if i % 2 == 0:
                pass_p += str(i) + " "
                total += i
    elif start_w > last_w:
        for i in range(start_w, last_w - 1, -1):
            if i % 2 == 0:
                pass_p += str(i) + " "
                total += i
    print("pass :", pass_p)
    print("Sum :", total)
 
main()