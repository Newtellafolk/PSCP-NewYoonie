"""Virus I"""
def scan():
    """print body of virus"""
    virus = str(input())
    virus = virus.replace("O", "")
    print(len(virus))

scan()
