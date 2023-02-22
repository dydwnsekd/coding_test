# 세그먼트 트리를 이용하는 방식으로 풀이가 필요
# 세그먼트 트리 https://m.blog.naver.com/ndb796/221282210534
# TODO
import sys

num_list = []
n, m, k = list(map(int, sys.stdin.readline().split()))

for _ in range(n):
    num_list.append(int(sys.stdin.readline()))

for _ in range(m+k):
    a, b, c = list(map(int, sys.stdin.readline().split()))

    if a == 1:
        num_list[b-1] = c
    elif a == 2:
        print(sum(num_list[b-1:c+1]))
