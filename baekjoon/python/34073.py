import sys

n = int(sys.stdin.readline())
sentence = sys.stdin.readline().strip().split(' ')

for s in sentence:
    print(s + "DORO", end=' ')
