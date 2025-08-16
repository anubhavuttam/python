import time
"""timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime"""

a = int(time.strftime('%H'))
print(a)
if (a<12):
    print("Good Morning Sir!")
elif(a>12 and a<16):
    print("Good Afternoon Sir!")
elif(a>16 and a<20):
    print("Good Evening Sir!")
elif(a>20 and a<24):
    print("Good Night Sir!")
else:
    print("Kis universe m jii rahe ho bhai?")
