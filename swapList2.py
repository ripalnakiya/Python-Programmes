# This is another version of the swapList.py

a = [2,4,6,8,0]

if len(a) % 2 == 0:
    half_1st = a[0 : len(a) // 2]
    middle = []
    half_2nd = a[len(a) // 2 : len(a)]
else:
    half_1st = a[0 : len(a) // 2]
    middle = []
    half_2nd = a[len(a) // 2 : len(a)]

b = half_2nd + middle + half_1st

print(b)
