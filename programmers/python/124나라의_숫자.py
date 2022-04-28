def solution(n):
    answer = ''
    num_124 = ['1','2','4']
    
    while True:
        if n > 3:
            answer = num_124[(n%3)-1] + answer
            n = n//3
        else:
            answer += num_124[n-1]
            break
    
    return answer