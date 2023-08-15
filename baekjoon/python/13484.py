import sys

remain_data = 0
default_data = int(sys.stdin.readline())
months = int(sys.stdin.readline())

for _ in range(months):
    remain_data += default_data - int(sys.stdin.readline())

print(default_data + remain_data)
