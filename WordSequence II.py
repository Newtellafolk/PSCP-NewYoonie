"""WordSequence II"""
def main():
    """WordSequence II"""
    txt_1 = input()
    txt_2 = input()
    for i in range(max((len(txt_1)), len(txt_2)) + 1):
        print(txt_2[:i] + txt_1[i:])
main()
