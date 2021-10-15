# https://programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    max_x = -999999
    max_y = -999999
    
    for i in sizes:
        i.sort()
        if i[0] > max_x:
            max_x = i[0]
        if i[1] > max_y:
            max_y = i[1]
        
    return max_x * max_y