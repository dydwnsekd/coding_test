import sys
from datetime import datetime

time_str1 = sys.stdin.readline().strip()
time_str2 = sys.stdin.readline().strip()

time1 = datetime.strptime(time_str1, "%H:%M:%S")
time2 = datetime.strptime(time_str2, "%H:%M:%S")

time_difference = time2 - time1

total_seconds = int(time_difference.total_seconds())
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

result = f"{hours:02}:{minutes:02}:{seconds:02}"
print(result)