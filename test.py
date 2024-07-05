# num = float('-1.0')			
# print(num)
# (come to my world)
# (come to my world)
# (come to my world)
# dg,eo

# """PickThem"""
# def main():
#     """PickThem"""
#     import json as j
#     word = input()
#     test = j.loads(word)
#     lekkoo = []
#     for answer in test:
#         if answer % 2 == 0:
#             lekkoo.append(answer)
#     if lekkoo == []:
#         print("Nope")
#     else:
#         for number in lekkoo:
#             print(number)
# main()

#     num = []
#     amount = int(input())
#     for _ in range(amount):
#         numin = float(input())
#         num.append(numin)
#     num.sort()
#     if amount % 2 == 1:
#         place = amount//2 + 1
#         print(num[place-1])
#     elif amount % 2 == 0:
#         place = amount//2
#         place2 = amount//2 + 1
#         answer = (num[place-1] + num[place2-1]) / 2
#         print(answer)

# """Ejudge"""
# def main():
#     """Diamond I"""
#     deep = int(input())
#     length = int(input())
#     diamond = []
#     value_daimond = []
#     for _ in range(deep):
#         value = input().split()
#         diamond.append(value)
#     for i in range(length):
#         cal = 0
#         for j in diamond:
#             cal += int(j[i])
#         value_daimond.append(cal)
#     print(max(value_daimond))
# main()

# greeting = ["hello"]
# tup = list(greeting)
# print(tup)

# s = 'abcdef'
# for a, b in enumerate(s, 1):
#     print(a, b)

def main():
    """T-Score"""
    X1, X2 = int(input()), int(input())
    L1 = [int(input()) for _ in range(X1)]
    A1 = sum(L1)/len(L1)
    S1 = ((len(L1) * sum([i**2 for i in L1]) - sum(L1)**2) / (len(L1)*(len(L1)-1)))**0.5
    L2 = ["%.2f" % (50+10*((i - A1)/S1)) for i in L1]
    print(*L2, sep="\n")