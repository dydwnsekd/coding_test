import sys
from collections import Counter

n = int(sys.stdin.readline())
num_list = []
for _ in range(n):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()
set_list = set(num_list)
many_count = 0
many_value = []

num_counter = Counter(num_list)
print(num_counter)

for k, v in num_counter.items():
    if many_count < v:
        many_count = v
        many_value = [k]
    elif many_count == v:
        many_value.append(k)

if len(many_value) == 1:
    many_value = many_value[0]
else:
    many_value.sort()
    many_value = many_value[1]

print(round(sum(num_list) / len(num_list)))
print(num_list[len(num_list)//2])
print(many_value)
print(max(num_list) - min(num_list))
