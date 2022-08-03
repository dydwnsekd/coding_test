import sys

def isInList(sorted_list, m):
    middle_index = len(sorted_list) // 2
    left = 0
    right = len(sorted_list) - 1

    while True:
        if m > sorted_list[middle_index]:
            left = middle_index + 1
            middle_index = (left + right) // 2
        elif m < sorted_list[middle_index]:
            right = middle_index - 1
            middle_index = (left + right) // 2
        elif m == sorted_list[middle_index]:
            return True
        if right <= left:
            return False

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()

m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

for i in m_list:
    if isInList(n_list, i):
        print("1", end=" ")
    else:
        print("0", end=" ")
