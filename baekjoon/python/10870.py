import sys

fibonacci = [0] * 21
fibonacci[0] = 0
fibonacci[1] = 1
fibonacci[2] = 1

for i in range(3,21):
    fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]

n = int(sys.stdin.readline())

print(fibonacci[n])
