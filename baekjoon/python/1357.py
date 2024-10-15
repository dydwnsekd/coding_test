import sys

x, y = sys.stdin.readline().strip().split()

x = int(x[::-1])
y = int(y[::-1])

result = x + y

print(int(str(result)[::-1]))
