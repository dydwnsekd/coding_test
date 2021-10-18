# https://programmers.co.kr/learn/courses/30/lessons/87390?language=python3
def solution(n, left, right):
    answer = []
    
    start_index = left // n + 1
    end_index = right - n * (start_index - 1) + 1
    
    # print(start_index)
    # print(end_index)
    
    for i in range(start_index, n+1):
        for j in range(1, n+1):
            if i >= j:
                answer.append(i)
            else:
                answer.append(j)
    
    # print(answer)
    return answer[left%n:end_index]