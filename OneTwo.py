"""OneTwo"""
def kidleak(leak):
    """One Two One Two call"""
    if leak in {1}:
        return "1"
    elif leak in {2}:
        return "2"
    return kidleak(leak - 1) + kidleak(leak - 2)

def main():
    """OneTwo"""
    print(kidleak(int(input())))

main()
