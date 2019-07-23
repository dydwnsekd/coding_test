import sys

div_num = list()

for _ in range(10):
    n = int(sys.stdin.readline())
    div_num.append(n%42)

print (len(set(div_num)))