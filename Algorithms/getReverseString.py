<<<<<<< HEAD
def getReverse(text):
    if len(text) == 0:
        return ""
    else:
        return getReverse(text[1:]) + text[0] # the first character is at the last position

=======
def getReverse(text):
    if len(text) == 0:
        return ""
    else:
        return getReverse(text[1:]) + text[0] # the first character is at the last position

>>>>>>> 69a79bbc7ebf13241089edb722e487619ff6f61f
print(getReverse("Hello"))