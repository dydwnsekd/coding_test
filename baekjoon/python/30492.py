import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().strip().split())
words = []
result = ""

for _ in range(n):
    words.append(sys.stdin.readline().strip())

for i in range(m):
    word_count = defaultdict(int)
    for j in range(n):
        word_count[words[j][i]] += 1

    print(word_count)


