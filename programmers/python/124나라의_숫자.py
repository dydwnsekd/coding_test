def solution(n):
    answer = ''
    num_124 = ['4','1','2']
    
    while n > 0:
        flag = False
        answer += num_124[n % 3]
        if n % 3 == 0:
            flag = True
        n = n // 3
    
        if flag:
            n -= 1
        
    return answer[::-1]