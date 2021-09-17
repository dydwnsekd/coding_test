# https://programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = []
    
    temp = arr[0]    
    for i in arr[1:]:
        if temp != i:
            answer.append(temp)
            temp = i
            
    if temp == arr[-1]:
        answer.append(arr[-1])
            
    return answer