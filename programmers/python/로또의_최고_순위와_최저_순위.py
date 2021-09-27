# https://programmers.co.kr/learn/courses/30/lessons/77484?language=python3
def solution(lottos, win_nums):
    answer = []
    
    correct_count = 0
    zero_count = 0
    
    for i in lottos:
        if i == 0:
            zero_count += 1
        elif i in win_nums:
            correct_count += 1
    
    if correct_count + zero_count > 1:
        answer.append(7-(correct_count+zero_count))
    else:
        answer.append(6)
        
    if correct_count > 1:
        answer.append(7-correct_count)
    else:
        answer.append(6)
    
    return answer