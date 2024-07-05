"""Duplicate I"""
def main():
    """Duplicate"""
    member_m = int(input())
    member_n = int(input())
    set_m = set()
    set_n = set()
    for _ in range(member_m):
        m_id = input()
        set_m.add(m_id)
    for _ in range(member_n):
        n_id = input()
        set_n.add(n_id)
    same = list(reversed(sorted(set_m.intersection(set_n))))
    if len(same) == 0:
        print("Nope")
    else:
        for i in same:
            print(i)

main()

# """Duplicate I"""
# def main():
#     """Duplicate I"""
#     member_m = int(input())
#     member_n = int(input())
#     list_m = []
#     list_n = []
#     for _ in range(member_m):
#         set_m = input()
#         list_m.append(set_m)

#     for _ in range(member_n):
#         set_n = input()
#         list_n.append(set_n)

#     same = set(list_m).intersection(set(list_n))
#     keep = sorted(same, reverse=True)

#     if len(keep) == 0:
#         print("Nope")
#     else:
#         for index in keep:
#             print(index)

# main()


