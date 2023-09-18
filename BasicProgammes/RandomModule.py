import random

# Genreate list of number from 1 to 10
# a = list(range(1, 11))


# generate random number between a and b (a and b both inclusive)
#print(random.randint(1, 100))


# create a list of 10 random numbers
# a = []
# for i in range(10):
#     a.append(random.randint(1, 100))


# list comprehension : generating list of 10 random numbers
a = [random.randint(1, 100) for i in range(10)]