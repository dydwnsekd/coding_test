import sys

num = int(sys.stdin.readline().split()[0])

for _ in range(num):
    input_ox = sys.stdin.readline().split()[0]

    result = 0
    score = 0
    for ox in input_ox:
        if ox == 'O':
            score += 1
            result += score
        else:
            score = 0

    print (result)


