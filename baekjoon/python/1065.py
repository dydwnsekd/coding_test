import sys

num = int(sys.stdin.readline())

count = 0

for i in range(1, num+1):
    flag = True

    str_num = str(i)
    if len(str_num) <= 2:
        count += 1
        
    else:
        diff = int(str_num[1]) - int(str_num[0])
        for j in range(2, len(str_num)):
            # print ("1", str_num)
            # print ("2", str_num[j])
            # print ("3", str_num[j-1])
            # print ("4", diff)
            if diff != int(str_num[j]) - int(str_num[j-1]):
                flag = False

        if flag:
            count += 1

print (count)
        