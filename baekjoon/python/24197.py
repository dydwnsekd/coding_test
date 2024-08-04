import sys

count = 0
tabs, current_tab = map(int, sys.stdin.readline().strip().split())
tab_list = list(map(int, sys.stdin.readline().strip().split()))
tab_count = len(tab_list)

for i in range(tab_count):
    print("(abs(current_tab - tab_list[i]):::", (abs(current_tab - tab_list[i])))
    print("tabs - current_tab + tab_list[i]:::", tabs - current_tab + tab_list[i])
    count += min(abs(current_tab - tab_list[i]), tabs - current_tab + tab_list[i])
    current_tab = min(abs(current_tab - tab_list[i]), tabs - current_tab + tab_list[i])

print(count)
