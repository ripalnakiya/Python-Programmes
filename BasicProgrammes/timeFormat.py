'''
convert 24 hour time format into 12 hour time format

input: time_24 = "2340"
output: time_12 = 11:40 PM

"0030" >> 12:30 AM
"0245" >> 2:25 AM
"1215" >> 12:15 PM
"1820" >> 6:20 PM

'''

time = input("Enter the 24 hour time: ")

hrs = int(time[0:2])
mins = time[2: ] # the blank will slice up to the end of the string, equal to time[2:4]

if hrs < 12:
    tag = "AM"
else:
    hrs = hrs - 12
    tag = "PM"
    
if hrs == 0:
    hrs = 12

print(f"{hrs}:{mins} {tag}")


