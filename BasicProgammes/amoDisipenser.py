import sys

amount = int(input("Enter the amount: "))

# validate the amount
if  amount < 0 or amount > 10000 or amount%100 != 0:
    sys.exit("Invalid Input")

a = amount//500
amount %= 500

b = amount//200
amount %= 200

c = amount//100
# amount %= 100 , No need to perform this because the remainder will be 0 only 
# resaon is because we already have checked the amount for multiple of 100

print(f"500 x {a} = {500*a}")
print(f"200 x {b} = {200*b}")
print(f"100 x {c} = {100*c}")

