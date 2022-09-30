import sys

convert_dict = {}
char_num = 10
result = 0
for i in range(65, 91):
    convert_dict[chr(i)] = char_num
    char_num += 1
for i in range(0, 11):
    convert_dict[str(i)] = i

num, n = sys.stdin.readline().split()
num = num[::-1]
n = int(n)

for i in range(len(num)):
    result += convert_dict[num[i]] * (n ** i)

print(result)