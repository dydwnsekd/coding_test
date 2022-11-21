import sys

fibonacci_list = [0] * 1002
fibonacci_list[1] = 1

for i in range(2, 1002):
    fibonacci_list[i] = fibonacci_list[i-1] + fibonacci_list[i-2]
    fibonacci_list[i] = fibonacci_list[i] % 1007

n = int(sys.stdin.readline())

print(fibonacci_list[n+1])
