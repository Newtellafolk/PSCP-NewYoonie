"""AlmostMean"""
def main():
    """_"""
    id_nisit = []
    score = []
    summ = 0
    score_index = 0
    amout = int(input())
    for _ in range(amout):
        id_pass = input().split()
        id_nisit.append(id_pass[0])
        score.append(float(id_pass[1]))
    for i in score:
        summ += float(i)
        mean = summ/amout
        sort_score = sorted(score)
    while True:
        if float(sort_score[score_index]) >= mean:
            score_index = score_index - 1
            break
        score_index = score_index + 1
    for i in range(len(score)):
        if float(score[i]) == float(sort_score[score_index]):
            print("%s\t%s" %(id_nisit[i], str(score[i])))
main()
