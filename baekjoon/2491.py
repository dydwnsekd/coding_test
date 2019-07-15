import sys

n = int(sys.stdin.readline())
length = 0
current_length = 0
pre_value = None
flag = True     # True = 커지고 있을 때, False = 작아지고 있을 때

num_list = list(map(int, sys.stdin.readline().split(" ")))

pre_value = num_list[0]

if n <= 2:
    print (n)
else:
    if num_list[0] < num_list[1]:
        
    for i in num_list[1:]:
        if flag == True and pre_value <= i:
            current_length += 1
        elif flag == True and pre_value > i:
            if current_length > length:
                length = current_length
            current_length = 0
        elif flag == False and pre_value >= i:
            current_length += 1
        else:
            if current_length > length:
                length = current_length
            current_length = 0
        pre_value = i

print (length)
    
        

