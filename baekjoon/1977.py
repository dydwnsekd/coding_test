import sys
import math

start_num = int(sys.stdin.readline())
end_num = int(sys.stdin.readline())

num_list = list()

for i in range(math.ceil(math.sqrt(start_num)), math.floor(math.sqrt(end_num))+1):
    num_list.append(i**2)


if len(num_list) != 0:
    print (sum(num_list))
    print (num_list[0])
else:
    print(-1)