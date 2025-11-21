import sys

n,m = map(int, sys.stdin.readline().strip().split())
predict_list = []

for _ in range(n):
    predict_list.append(list(map(int, sys.stdin.readline().strip().split())))

for _ in range(m):
    count = 0
    g, x, y = map(int, sys.stdin.readline().strip().split())

    for i in range(n):
        if g >= predict_list[i][0] and x <= predict_list[i][1] and y <= predict_list[i][2]:
            count += 1

    print(count)


