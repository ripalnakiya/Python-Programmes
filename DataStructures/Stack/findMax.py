<<<<<<< HEAD
import random
import stack

def main():
    a = [random.randint(1, 100) for i in range(10)]
    print(a)
    print(getMax(a))

def getMax(a):
    s = stack.stack()
    for i in range(len(a)):
        s.push(a[i])

    mxnum = s.pop()

    while(not s.isEmpty()):
        if (s.peek() > mxnum):
            mxnum = s.pop()
        else :
            s.pop()

    return mxnum

=======
import random
import stack

def main():
    a = [random.randint(1, 100) for i in range(10)]
    print(a)
    print(getMax(a))

def getMax(a):
    s = stack.stack()
    for i in range(len(a)):
        s.push(a[i])

    mxnum = s.pop()

    while(not s.isEmpty()):
        if (s.peek() > mxnum):
            mxnum = s.pop()
        else :
            s.pop()

    return mxnum

>>>>>>> 69a79bbc7ebf13241089edb722e487619ff6f61f
main()