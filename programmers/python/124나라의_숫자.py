def solution(n):
    answer = ''
    num_124 = ['4','1','2']
    
    while True:
        flag = False
        if n > 3:
            if n % 3 == 0:
                flag = True
                
            answer += num_124[n % 3]
            n = n // 3
        
            if flag:
                n -= 1
        else:
            answer += num_124[n % 3]
            break
    
    return answer[::-1]

print(solution(6))