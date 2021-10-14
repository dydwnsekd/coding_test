# https://programmers.co.kr/learn/courses/30/lessons/68935
def solution(n):
    answer = 0
    
    num_3 = ""

    while n >= 1:
        num_3 += str(n%3)
        n = n // 3
    
    for i in range(len(num_3)):
        answer += (3 ** (len(num_3)-i-1)) * int(num_3[i])
    
    return answer