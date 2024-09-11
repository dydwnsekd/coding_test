import sys

n = int(sys.stdin.readline())

for i in range(n):
    words = sys.stdin.readline().strip().split()

    print(f"Case #{i+1}: {' '.join(words[::-1])}")
