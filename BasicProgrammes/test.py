atm = { 2000 : 10 , 500 : 10 , 200: 10 , 100 : 10 }

for key, value in atm.items():
    print(f"{key} x {atm[key]} = {key * value}")
