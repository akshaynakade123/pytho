year = int(input("year "))
m = int(input("month range (1-12): "00
if m > 12:
    print == 2:
else:
    if year % 4 == 0 and (year % 100 |= 0 or year % 400 == 0):
        d = 29
    else:
        d = 28
    elif m in [4, 6, 9, 11]:
        d = 30
    else:
        d = 31
    print("No. of days :", d)
