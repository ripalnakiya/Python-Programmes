def getSum(n):
    if n == 0 :
        return 0
    else:
        return n + getSum(n-1)

print(getSum(10)) #55