import sys

N, m, M, T, R = map(int, sys.stdin.readline().strip().split())
total_time = 0
working_time = 0
current_m = m

while True:
    if current_m + T > M:
        total_time += 1
        if current_m - R < m:
            current_m = m
        else:
            current_m -= R

    else:
        working_time += 1
        total_time += 1
        current_m += T

    if working_time >= N:
        break

print(total_time)
