"""iPhone13 Again"""
def calprice(model, capa):
    """cal price of each model"""
    if model == "iPhone 13 mini":
        print(imini(model, capa))
    elif model == "iPhone 13":
        print(isibsarm(model, capa))
    elif model == "iPhone 13 Pro":
        print(ipro(model, capa))
    elif model == "iPhone 13 Pro Max":
        print(ipromax(model, capa))
    else:
        print("Not Available")

def imini(model, capa):
    """iPhone13 mini"""
    if model == "iPhone 13 mini":
        if capa == "128 GB":
            return 25900
        elif capa == "256 GB":
            return 29900
        elif capa == "512 GB":
            return 37900
        else:
            return "Not Available"

def isibsarm(model, capa):
    """iPhone13"""
    if model == "iPhone 13":
        if capa == "128 GB":
            return 29900
        elif capa == "256 GB":
            return 33900
        elif capa == "512 GB":
            return 41900
        else:
            return "Not Available"

def ipro(model, capa):
    """iPhone13 Pro"""
    if model == "iPhone 13 Pro":
        if capa == "128 GB":
            return 38900
        elif capa == "256 GB":
            return 42900
        elif capa == "512 GB":
            return 50900
        elif capa == "1 TB":
            return 58900
        else:
            return "Not Available"

def ipromax(model, capa):
    """iPhone13 Pro Max"""
    if model == "iPhone 13 Pro Max":
        if capa == "128 GB":
            return 42900
        elif capa == "256 GB":
            return 46900
        elif capa == "512 GB":
            return 54900
        elif capa == "1 TB":
            return 62900
        else:
            return "Not Available"

calprice(input(), input())
