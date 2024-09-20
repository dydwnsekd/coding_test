import sys

fibonacci = [0, 1]

for i in range(2, 50):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print(fibonacci[int(sys.stdin.readline())])
