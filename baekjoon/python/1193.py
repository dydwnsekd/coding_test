# TODO
n = int(input())
counter = 2
sum_num_list = [1]
temp = 2

while sum_num_list[-1] < 10000000:
    sum_num_list.append(temp)
    temp += counter
    counter += 1

for i in range(len(sum_num_list)):
    if n >= sum_num_list[i]:
        print(f"/{i-1}")
