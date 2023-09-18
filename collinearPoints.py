data = input("Enter the coordinate 1: ") # x,y
x1,y1 = data.split(",")
x1 = int(x1)
y1 = int(y1)

data = input("Enter the coordinate 2: ") # x,y
x2,y2 = data.split(",")
x2 = int(x2)
y2 = int(y2)

data = input("Enter the coordinate 3: ") # x,y
x3,y3 = data.split(",")
x3 = int(x3)
y3 = int(y3)

area = 1/2 * (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

if area == 0: print("Collinear")
else: print("Not collinear")