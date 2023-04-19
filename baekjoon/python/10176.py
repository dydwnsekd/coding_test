import sys

cases = int(sys.stdin.readline())
reverse_words = list("abcdefghijklmnopqrstuvwxyz")
print(reverse_words)

for _ in range(cases):
    words = sys.stdin.readline().strip().lower()
