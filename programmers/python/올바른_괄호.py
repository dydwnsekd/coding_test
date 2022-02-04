def solution(s):
    answer = True
    c = 0
    
    for i in s:
        if i == "(":
            c += 1
        else:
            c -= 1
        
        if c < 0:
            break
            
    if c != 0:
        answer = False

    return answer