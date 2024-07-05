"""RockPaperScissor"""
def main():
    """who is the winner"""
    pao, nai_a, nai_b = input(), int(), int()
    for i in range(0, len(pao), 2):
        if pao[i] == pao[i+1]:
            pass
        elif pao[i] == "R" and pao[i+1] == "S" or pao[i] == "S" and pao[i+1] == "P" or \
pao[i] == "P" and pao[i+1] == "R":
            nai_a += 1
        else:
            nai_b += 1
    if nai_a > nai_b:
        print("A win %d-%d" %(nai_a, nai_b))
    elif nai_b > nai_a:
        print("B win %d-%d" %(nai_b, nai_a))
    else:
        print("DRAW %d" %nai_a)

main()
