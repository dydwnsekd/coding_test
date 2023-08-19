import sys

flag = True
triangle_1 = list(map(int, sys.stdin.readline().split()))
triangle_2 = list(map(int, sys.stdin.readline().split()))

triangle_1.sort()
triangle_2.sort()

if triangle_1[0]**2 + triangle_1[1]**2 != triangle_1[2]**2:
    flag = False

if triangle_2[0]**2 + triangle_2[1]**2 != triangle_2[2]**2:
    flag = False

if triangle_1[0] != triangle_2[0] or triangle_1[1] != triangle_2[1]:
    flag = False

if flag:
    print("YES")
else:
    print("NO")
