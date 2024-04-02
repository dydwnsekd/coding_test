import sys

n = int(sys.stdin.readline())
sum_n = 0
sum_n_2 = 0
sum_n_3 = 0

for i in range(1, n+1):
    sum_n += i
    sum_n_2 += i
    sum_n_3 += i ** 3

print(sum_n)
print(sum_n_2 ** 2)
print(sum_n_3)
