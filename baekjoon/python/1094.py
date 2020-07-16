import sys

x = int(sys.stdin.readline())
count = 0

bin_x = bin(x)[2:]

for i in bin_x:
    if i == '1':
        count += 1

print (count)