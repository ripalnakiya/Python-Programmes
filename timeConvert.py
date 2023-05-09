time = int(input("Seconds: "))

min, sec = time // 60, time % 60

#min, sec = divmod(sec, 60)

if min < 10:
    min = '0' + str(min)

if sec < 10:
    sec = '0' + str(sec)

print(min , ':' , sec)