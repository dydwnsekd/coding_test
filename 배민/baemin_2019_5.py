# -*- coding: utf-8 -*-

'''
a = 100000
b = ""
count = 0

for i in range(1, a+1):
    b = "%s%s" % (b, i)

for i in b:
    if i in ['3','6','9']:
        count = count + 1

print (count)
'''

# 100까지 60
# 1000까지 900
# 10000까지 12000
# 100000까지 150000


def solution(num):
    i = 0
    num_list = [100000, 10000, 1000, 100, 10]
    value_list = [150000, 12000, 900, 60, 3]

    count = 0

    while i<5:
        if num/num_list[i] >= 9:
            count = count + num_list[i] * 3
        elif num/num_list[i] >= 6:
            count = count + num_list[i] * 2
        elif num/num_list[i] >= 3:
            count = count + num_list[i]
        count = count + (value_list[i] * (num/num_list[i]))
        num = num%num_list[i]
        i = i+1

    for i in range(1, num+1):
        if i in [3,6,9]:
            count = count + 1

    print (count)

if __name__ == "__main__":
    solution(43)