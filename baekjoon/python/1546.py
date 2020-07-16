import sys

num = int(sys.stdin.readline().split()[0])

num_list = list(map(int, input().rstrip().split()))

num_list.sort()
max_value = num_list[-1]

result = 0

for i in range(num):
    result += num_list[i]/max_value * 100

print (result/num)
