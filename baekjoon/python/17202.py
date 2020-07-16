import sys

num1 = sys.stdin.readline().replace("-", "").replace("\n", "")
num2 = sys.stdin.readline().replace("-", "").replace("\n", "")

num = ""
temp = "0000000000"

for i in range(len(num1)):
    num = num + num1[i]
    num = num + num2[i]

while(len(num) >= 3):
    temp = ""
    for i in range(len(num)-1):
        weight = (int(num[i]) + int(num[i+1])) % 10
        temp += str(weight)

    num = temp

print (num)