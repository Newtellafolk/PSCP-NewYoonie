"""[Recommended] WPM"""
def result():
    """[Recommended] WPM"""
    agee = input()
    wpmm = int(input())
    if agee == "Kids":
        print(kids(agee, wpmm))
    elif agee == "Adults":
        print(adults(agee, wpmm))

def kids(agee, wpmm):
    """kid"""
    if agee == "Kids":
        if wpmm < 11:
            return "Very Slow"
        elif 11 <= wpmm <= 20:
            return "Slow"
        elif 21 <= wpmm <= 30:
            return "Average"
        elif 31 <= wpmm <= 40:
            return "Fast"
        else:
            return "Very Fast"

def adults(agee, wpmm):
    """adult"""
    if agee == "Adults":
        if wpmm < 26:
            return "Very Slow"
        elif 26 <= wpmm <= 35:
            return "Slow/Beginner"
        elif 36 <= wpmm <= 45:
            return "Intermediate/Average"
        elif 46 <= wpmm <= 65:
            return "Fast/Advanced"
        elif 66 <= wpmm <= 80:
            return "Very Fast"
        else:
            return "Insane"
result()
