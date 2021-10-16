# https://programmers.co.kr/learn/courses/30/lessons/87390?language=python3
def solution(n, left, right):
    answer = []
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i >= j:
                answer.append(i)
            else:
                answer.append(j)     
        
    return answer[left:right+1]