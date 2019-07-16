import sys

n = int(sys.stdin.readline())
length = 0
current_length = 1
equal_length = 0
pre_value = None
flag = None     # True = 커지고 있을 때, False = 작아지고 있을 때

num_list = list(map(int, sys.stdin.readline().split(" ")))

pre_value = num_list[0]

if n <= 2:
    length = n

else:
    for i in num_list[1:]:
        if pre_value < i:
            if flag != False:
                current_length += 1
            else:
                if current_length > length:
                    length = current_length
                    current_length = 2
                    current_length += equal_length
                    equal_length = 0
            flag = True

        elif pre_value == i:
            if equal_length == 0:
                equal_length = 1
            else:
                equal_length += 1
            current_length += 1
            
        else:
            if flag != True:
                flag = False
                current_length += 1
            else:
                if current_length > length:
                    length = current_length
                    current_length = 2
                    current_length += equal_length
                    equal_length = 0
            flag = False
            
        pre_value = i
    
        # print ('i', i)
        # print ('current', current_length)
        # print ('length', length)
        # print ('equal', equal_length)
        # print ('\n')

if current_length > length:
    length = current_length

print (length)