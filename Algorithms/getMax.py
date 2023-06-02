from random import randint

def getMax(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        a = nums[0]
        b = getMax(nums[1:])
        if a > b:
            return a
        return b


a = [randint(1, 100) for i in range(10)]
print(a)
print(getMax(a))