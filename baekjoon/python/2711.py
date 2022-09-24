import sys

n = int(sys.stdin.readline())

for _ in range(n):
    i, word = list(sys.stdin.readline().split())
    print(word[:int(i)-1]+word[int(i):])
