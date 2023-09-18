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
    amount = int(input("Enter the value: "))
    denominations(amount)


def denominations(amount):
    n1, n2, n3, n4 = 2000, 500, 200, 100

    if amount <= 1000:
        d = 1
    else:
        d = 5

    amount = amount - (n4*d)

    a = amount // n1
    amount = amount % n1

    b = amount // n2
    amount = amount % n2

    c = amount // n3
    amount = amount % n3

    d = d + amount // n4

    print(f"{n1} x {a} = {n1*a}")
    print(f"{n2} x {b} = {n2*b}")
    print(f"{n3} x {c} = {n3*c}")
    print(f"{n4} x {d} = {n4*d}")

if __name__ == "__main__":
    main()