"""RemoveTag"""
def main():
    """RemoveTag"""
    txt = input().replace("<", "$<").replace(">", ">$").split("$")
    new_lst = []
    for i in txt:
        if "<" in i and ">" in i:
            continue
        new_lst.extend(i.split())
    print(new_lst)
main()
