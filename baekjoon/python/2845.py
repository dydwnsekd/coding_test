import sys

l, p = list(map(int, sys.stdin.readline().split()))
human_count = l*p

p = list(map(int, sys.stdin.readline().split()))
for i in p:
    print(human_count-i, end=" ")
