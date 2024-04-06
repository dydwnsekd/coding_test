import sys

def get_grade(rank: int):
    if rank <= 4:
        return 1
    elif rank <= 11:
        return 2
    elif rank <= 23:
        return 3
    elif rank <= 40:
        return 4
    elif rank <= 60:
        return 5
    elif rank <= 77:
        return 6
    elif rank <= 89:
        return 7
    elif rank <= 96:
        return 8
    elif rank <= 100:
        return 9

result = []

n, k = map(int, sys.stdin.readline().strip().split())
d_list = list(map(int, sys.stdin.readline().strip().split()))

for i in d_list:
    result.append(get_grade((i*100) // n))

print(*result)
