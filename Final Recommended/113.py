"""113"""
def remove_113(laek):
    """113"""
    while "113" in laek:
        laek = laek.replace("113", "", 1)
    return laek

def main():
    """result"""
    laek = input()
    print(remove_113(laek))
main()


