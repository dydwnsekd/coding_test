import sys

koong = [0 for i in range(69)]
koong[0] = 1
koong[1] = 1
koong[2] = 2
koong[3] = 4
for i in range(4, 69):
    koong[i] = koong[i-1] + koong[i-2] + koong[i-3] + koong[i-4]

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    print(koong[int(sys.stdin.readline())])
