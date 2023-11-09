# commit 대기
import sys

result = 0
n = int(sys.stdin.readline())

for i in range(1, n+1):
    result += i ** 3

print(result)

