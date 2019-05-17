import sys

num1 = sys.stdin.readline().replace("-", "")
num2 = sys.stdin.readline().replace("-", "")

num = ""
temp = "0000000000"

for i in range(len(num1)):
    num = num + num1[i]
    num = num + num2[i]

print (num)
while(len(num) >= 2):
    temp = ""
    for i in range(len(num)-2):
        print (num[i])
        print (num[i+1])
        weight = int(num[i]) + int(num[i+1])
        if weight > 10:
            weight -= 10
        
        temp += str(weight)
    
    print (temp)
    num = temp

print (num)