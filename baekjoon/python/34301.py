import sys

n = int(sys.stdin.readline())
change_list = []
dollars = [150, 30, 15, 5, 1]

for dollar in dollars:
    change_list.append(n // dollar)
    n = n % dollar

change_list.reverse()
print(*change_list)

