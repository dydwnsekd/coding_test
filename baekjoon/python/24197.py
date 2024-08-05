import sys

count = 0
current_tab = 1
n, m = map(int, sys.stdin.readline().strip().split())
tab_list = list(map(int, sys.stdin.readline().strip().split()))
tab_count = len(tab_list)

for i in range(tab_count):
    count += min((current_tab - tab_list[i] + n) % n, (tab_list[i] - current_tab + n) % n)
    current_tab = tab_list[i]

print(count)
