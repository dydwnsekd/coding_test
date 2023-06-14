import sys

adjectives = []
nouns = []

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

for _ in range(n):
    adjectives.append(sys.stdin.readline().strip())

for _ in range(m):
    nouns.append(sys.stdin.readline().strip())

for i in range(n):
    for j in range(m):
        print(f"{adjectives[i]} as {nouns[j]}")
