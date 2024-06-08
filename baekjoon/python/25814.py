import sys

a_weight = 0
b_weight = 0
a, b = sys.stdin.readline().strip().split()

for i in a:
    a_weight += int(i)

for i in b:
    b_weight += int(i)

a_weight *= len(a)
b_weight *= len(b)

if a_weight > b_weight:
    print(1)
elif a_weight < b_weight:
    print(2)
else:
    print(0)
