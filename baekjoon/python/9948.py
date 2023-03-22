import sys
from datetime import datetime

month_dict = {"January": "1", "February": "2", "March": "3", "April": "4", "May": "5", "June": "6",
              "July": "7", "August": "8", "September": "9", "October": "10", "November": "11", "December": "12"}
today = datetime(2007, 8, 4)

while True:
    day, month = sys.stdin.readline().strip().split()
    if day == "0" and month == "#":
        break

    month = month_dict[month]
    try:
        dt = datetime.strptime(f"2007-{month}-{day}", "%Y-%m-%d")
        if dt < today:
            print("Yes")
        elif dt == today:
            print("Happy birthday")
        else:
            print("No")
    except:
        print("Unlucky")


