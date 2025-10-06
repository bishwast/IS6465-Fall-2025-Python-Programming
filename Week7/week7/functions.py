# Yes No Boolean Converter
def yesNoBooleanConverter(val):
    val = str(val).upper()
    if val == "Y" or val == "YES":
        return True
    else:
        return False

def booleanYesNoConverter(val):
    if val:
        return "Yes"
    return "No"

# null
def nullToBooleanConverter(val):
    return val != None  # True, IF NOT None returns False

def moveQueueValueConverter(val):
    """R = Released, H = Hold, D = Deleted, P = Pending"""
    val = str(val).upper()
    if val == "R":
        return "Released"
    elif val == "H":
        return "Hold"
    elif val == "D":
        return "Deleted"
    elif val == "P":
        return "Pending"
    else: return None

