import sys

k, v = list(map(int, sys.stdin.readline().split(" ")))

num_list = [i for i in range(1,k+1)]
origin_len = len(num_list)
result_list = list()

index = 0

while len(result_list) != origin_len:
    remove_index = (index+v-1) % len(num_list)
    result_list.append(num_list.pop(remove_index))
    
    if remove_index == len(num_list):
        index = 0
    else:
        index = remove_index

print ('<', end='')
for i in range(len(result_list)):
    if i == len(result_list) - 1:
        print (result_list[i], end="")
    else:
        print (result_list[i], end=", ")
print ('>')
