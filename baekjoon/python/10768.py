import sys
from datetime import datetime

month = int(sys.stdin.readline())
day = int(sys.stdin.readline())

# if month < 2:
#     print("Before")
# elif month == 2:
#     if day < 18:
#         print("Before")
#     elif day == 18:
#         print("Special")
#     else:
#         print("After")
# else:
#     print("After")

special_date = datetime(2015, 2, 18)
input_date = datetime(2015, month, day)

if special_date > input_date:
    print("Before")
elif special_date == input_date:
    print("Special")
else:
    print("After")
