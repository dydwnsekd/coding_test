# https://programmers.co.kr/learn/courses/30/lessons/87390?language=python3

def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1)
    return answer

"""
def solution(n, left, right):
    answer = []
    
    start_index = left // n + 1
    end_index = right - n * (start_index - 1) + 1
    
    for i in range(start_index, n+1):
        for j in range(1, n+1):
            if len(answer) < (right - left) * 2:
                if i >= j:
                    answer.append(i)
                else:
                    answer.append(j)
            else:
                break
    
    return answer[left%n:end_index]
"""