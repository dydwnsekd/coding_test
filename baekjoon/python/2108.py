import sys

n = int(sys.stdin.readline())
num_list = []
for _ in range(n):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()
set_list = set(num_list)
many_count = 0
many_value = None

for i in set_list:
    if num_list.count(i) > many_count:
        many_value = i

print(round(sum(num_list) / len(num_list)))
print(num_list[len(num_list)//2])
print(many_value)
print(max(num_list) - min(num_list))
