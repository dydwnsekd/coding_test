#https://www.acmicpc.net/problem/1019
import sys

n = int(sys.stdin.readline())
num_list = []
result_list = [0] * 10

for i in range(1, n+1):
    str_num = str(i)
    for j in str_num:
        result_list[int(j)] += 1

#https://mygumi.tistory.com/180
#https://www.slideshare.net/Baekjoon/baekjoon-online-judge-1019
while(True):
    temp = n%10
    n = int(n/10)
    print (n)
    num_list.append(temp)
    
    if n<10:
        num_list.append(n)
        break

for i in result_list:
    print (i, end=' ')