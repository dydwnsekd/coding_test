import sys

cases = int(sys.stdin.readline())
print(15000 - len(set(sys.stdin.readline().split())))
