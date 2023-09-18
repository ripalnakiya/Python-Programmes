list = [2,4,6,8,0]

#  0  1  2  3  4  5
#  2  4  6  8  0  3

# output
# 8 0 6 2 4

length = len(list)
num = length // 2

if length % 2 == 0:
    j = num
else:    
    j = num + 1

for i in range (num):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
    j += 1

print(list)

