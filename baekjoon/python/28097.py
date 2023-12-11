import sys

result = 0

cases = int(sys.stdin.readline())

result += sum(list(map(int, sys.stdin.readline().split())))
result += 8 * (cases - 1)

print(f"{result // 24} {result % 24}")
