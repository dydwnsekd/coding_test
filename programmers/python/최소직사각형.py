# https://programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    answer = 0
    
    x = []
    y = []
    
    for i in sizes:
        i.sort()
        print (i)
        x.append(i[0])
        y.append(i[1])
        
    x.sort()
    y.sort()
    
    return x[-1] * y[-1]