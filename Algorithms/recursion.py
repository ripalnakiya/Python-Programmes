def counter(n):
    if n==0:
        pass
    else:
        counter(n-1)
        print(n)

counter(5)