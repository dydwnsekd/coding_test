import sys

count = 0
n = int(sys.stdin.readline())
words = sys.stdin.readline().strip().split()

for w in words:
    if w in ["he", "she", "him", "her"]:
        count += 1

print(count)
