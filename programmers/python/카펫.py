# https://programmers.co.kr/learn/courses/30/lessons/42842?language=python3

def solution(brown, yellow):
    sum_xy = brown/2 + 2
    
    if sum_xy % 2 == 1:
        x = int(sum_xy//2)+1
    else:
        x = int(sum_xy//2)
    y = int(sum_xy//2)
    
    area = brown + yellow
    
    while(True):
        if x*y == area:
            break
        else:
            x += 1
            y -= 1
    
    answer = [x,y]
    return answer