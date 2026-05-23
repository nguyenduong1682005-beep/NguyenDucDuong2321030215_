import datetime
now = datetime.datetime.now()
print(now)
s = now.strftime("%d/%m/%y, %H:%M:%S")
print("s: ", s)