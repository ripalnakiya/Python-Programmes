def getReverse(text):
    if len(text) == 0:
        return ""
    else:
        return getReverse(text[1:]) + text[0] # the first character is at the last position

print(getReverse("Hello"))