"""T-score"""
def main():
    """T-score"""
    student, full_score = int(input()), int(input())
    stu_score = [int(input()) for _ in range(student)]
    average = sum(stu_score)/len(stu_score)
    cal = ((len(stu_score) * sum([i**2 for i in stu_score]) - \
sum(stu_score)**2) / (len(stu_score)*(len(stu_score)-1)))**0.5
    t_score = ["%0.2f" %(50+10*((i - average)/cal)) for i in stu_score]
    print(*t_score, sep="\n")
main()
