import sys

zero_result = [0 for i in range(41)]
one_result = [0 for i in range(41)]

zero_result[0] = 1
zero_result[1] = 0

one_result[0] = 0
one_result[1] = 1

for i in range(2, 41):
    zero_result[i] = zero_result[i-1] + zero_result[i-2]
    one_result[i] = one_result[i-1] + one_result[i-2]

num_count = int(sys.stdin.readline())

for _ in range(num_count):
    num = int(sys.stdin.readline())
    print("%d %d" % (zero_result[num], one_result[num]))
