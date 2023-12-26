import sys

bread, patty = list(map(int, sys.stdin.readline().split()))

print(min(bread // 2, patty))
