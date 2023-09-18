# This is optimized version of amoDispenserMod.py file

amount = int(input("Enter the value: "))

atm = { 2000 : 10 , 500 : 10 , 200: 10 , 100 : 10 }
cash = { 2000 : 0 , 500 : 0 , 200: 0 , 100 : 0 }

if amount <= 1000:
    cash[100] += 1
    atm[100] -= 1
else:
    cash[100] += 5
    atm[100] -= 5
amount -= (100 * cash[100])

for (key1,value1), (key2,value2) in zip(atm.items(), cash.items()):
    cash[key2] += amount // key2
    atm[key1] -= amount // key2
    amount %= key2

for key, value in cash.items():
    print(f"{key} x {value} = {key * value}")

print("Remaining notes in atm: ")
for key, value in atm.items():
    print(f"{key} x {value} = {key * value}")