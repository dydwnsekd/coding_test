import sys

result_arr = [0 for _ in range(1000001)]
result_arr[1] = 0

for i in range(2, 1000001):
    c = 9999999999
    if i % 3 == 0:
        index = int(i/3)
        if c > result_arr[index]:
            c = result_arr[index]
    
    if i % 2 == 0:
        index = int(i/2)
        if c > result_arr[index]:
            c = result_arr[index]
    
    if c > result_arr[i-1]:
        c = result_arr[i-1]

    result_arr[i] = c+1
    
num = int(sys.stdin.readline())

print (result_arr[num])
