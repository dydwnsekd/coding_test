import sys

sys.stdin.readline()

n = set(map(int, sys.stdin.readline().split()))
m = set(map(int, sys.stdin.readline().split()))

print(len((m-n)))
