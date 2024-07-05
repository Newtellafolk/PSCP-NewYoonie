"""Run Game"""
def main():
    """Run Game"""
    tmp = 0
    keep_val = 0
    distancee = input().split()
    for i in distancee:
        currnt_item = int(i)
        tmp = abs(currnt_item - tmp)
        keep_val += tmp
        tmp = currnt_item
    print(keep_val)




main()
