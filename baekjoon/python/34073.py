import sys

n = int(sys.stdin.readline())
sentence = sys.stdin.readline().strip().split(' ')

print(" ".join(s + "DORO" for s in sentence))
