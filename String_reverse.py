import sys

input_str = sys.stdin.readline().rstrip().split(" ")
str_len = len(input_str)
reverse_str = []

for i in range(str_len-1, -1, -1):
    reverse_str.append(input_str[i])

print (reverse_str)