def is_isogram(string):
    li_ss = (string.lower())
    letters = [ch for ch in li_ss if ch.isalpha()]
    
    if len(letters) == len(set(letters)):
        return True
    else:
        return False