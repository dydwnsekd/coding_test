# https://programmers.co.kr/learn/courses/30/lessons/86051?language=python3
def solution(numbers):
    num_list = [i for i in range(10)]
    answer = sum(num_list)
    
    for i in numbers:
        answer -= i
        
    return answer