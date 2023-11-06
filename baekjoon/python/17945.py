import sys, math

answer = []

a = 1
b, c = map(int, sys.stdin.readline().split())

answer.append(int(((-2*b) + math.sqrt(((2*b) ** 2) - 4*c)) // 2))
answer.append(int(((-2*b) - math.sqrt(((2*b) ** 2) - 4*c)) // 2))

answer.sort()

if answer[0] == answer[1]:
    print(answer[0])

else:
    print(*answer)

