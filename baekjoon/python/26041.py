import sys

count = 0

num_list = sys.stdin.readline().strip().split()
find_num = sys.stdin.readline().strip()

for num in num_list:
    if num.startswith(find_num) and num != find_num:
			  count += 1

print(count)



