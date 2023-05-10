import sys

date = (input("Date: ")) #yyyy-MM-dd

y, m, d = date.split('-')
# date string is spillted at '-' into list of three strings

y=int(y)
m=int(m)
d=int(d)

if y < 0 and y > 2023:
    sys.exit("Incorrect")

if m < 0 and m > 12:
    sys.exit("Incorrect")

if d < 0:
    sys.exit("Incorrect")

if m == 2:
    if (y % 4 == 0 and y % 100!= 0) or y % 400 == 0:
        if d > 29:
            sys.exit("Incorrect")
    elif d > 28:
        sys.exit("Incorrect")

elif m == 4 or m == 6 or m == 9 or m == 11:
    if d > 30:
        sys.exit("Incorrect")

else:
    if d > 31:
        sys.exit("Incorrect")

print("Date is valid")