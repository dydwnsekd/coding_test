import sys

while(True):
    num_list = list(map(int, sys.stdin.readline().split(" ")))
    max_value = max(num_list)
    min_value = min(num_list)
    
    c = max_value ** 2
    a = 0

    if (max_value == min_value == 0):
        break

    for i in num_list:
        if i != max_value:
            a += i**2
            
    if a == c:
        print("right")
    else:
        print("wrong")
    