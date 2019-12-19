def solution(n, lost, reserve):
    
    for i in reserve:
        if (i) in lost:
            lost.pop(lost.index(i))
            reserve.pop(reserve.index(i))
    for i in reserve:
        if (i-1) in lost:
            lost.pop(lost.index(i-1))
        elif (i+1) in lost:
            lost.pop(lost.index(i+1))
    
    answer = (n - len(lost))
    return answer