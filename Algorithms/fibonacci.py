<<<<<<< HEAD
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        c = fib(n-1) + fib(n-2)
        return c
    

# Using the memoisation approach : Highly efficient    
result = {}
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        if n in result:
            c = result[n]
        else:
            c = fib(n-1) + fib(n-2)
            result[n] = c
        return c
    
=======
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        c = fib(n-1) + fib(n-2)
        return c
    

# Using the memoisation approach : Highly efficient    
result = {}
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        if n in result:
            c = result[n]
        else:
            c = fib(n-1) + fib(n-2)
            result[n] = c
        return c
    
>>>>>>> 69a79bbc7ebf13241089edb722e487619ff6f61f
print(fib(30))