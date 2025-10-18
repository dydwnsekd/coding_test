import sys

n = sys.stdin.readline().strip()
champernowne_flag = True
find_num = '1'
find_index = 0

while True:
    if n[find_index:find_index+len(find_num)] == find_num:
        find_num = str(int(find_num) + 1)
    else:
        champernowne_flag = False
        break

if champernowne_flag:
    print(find_num)
else:
    print(-1)
