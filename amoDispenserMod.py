'''
Input an amount from the user 
and express the amount in the form of following denominations
2000, 500, 200, 100

if amount   1000 or less : minimum 1 note of 100
            more than 1000 : minimum 5 notes of 100

Input: 5900
Output:
2000 x 2 = 4000
500 x 2 = 1000
200 x 2 = 400
100 x 5 = 500
'''

def main():
    n = int(input("Enter the value: "))
    denominations(n)


def denominations(n):
    n1, n2, n3, n4 = 2000, 500, 200, 100

    if n <= 1000:
        d = 1
    else:
        d = 5

    n = n - (n4*d)

    a = n // n1
    n = n % n1

    b = n // n2
    n = n % n2

    c = n // n3
    n = n % n3

    d = d + n // n4

    print(f"{n1} x {a} = {n1*a}")
    print(f"{n2} x {b} = {n2*b}")
    print(f"{n3} x {c} = {n3*c}")
    print(f"{n4} x {d} = {n4*d}")

main()

