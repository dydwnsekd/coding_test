import sys

parstel = [30, 40]
parscell = [35, 30]
parsphone = [40, 20]

sim = [[30, 40], [35, 30], [40, 20]]

while True:
    c, d = list(map(int, sys.stdin.readline().split()))
    if c == 0 and d == 0:
        break
    else:
        min_value = 999999
        for s in sim:
            temp = s[0] * c + s[0] * d
            if temp < min_value:
                min_value = temp
        print(min_value)

