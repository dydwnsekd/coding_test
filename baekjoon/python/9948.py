import sys

birthday_month = ["January", "February", "March", "April", "May", "June", "July"]
non_birthday_month = ["September", "October", "November", "December"]

while True:
    day, month = sys.stdin.readline().strip().split()
    if day == "0" and month == "#":
        break
    elif day == "29" and month == "February":
        print("Unlucky")
    elif day == "4" and month == "August":
        print("Happy birthday")
    elif int(day) < 4 and month == "August":
        print("Yes")
    elif int(day) > 4 and month == "August":
        print("No")
    elif month in birthday_month:
        print("Yes")
    else:
        print("No")
