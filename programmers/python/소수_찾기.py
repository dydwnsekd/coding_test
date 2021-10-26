# https://programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    sieve = [True] * (n+1)

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n+1, i):
                sieve[j] = False

    return sieve[2:].count(True)
    
"""
def isdecimal(n):
    if n == 2 or n == 3:
        return True
    
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True

def solution(n):
    answer = 0
    
    for i in range(2, n+1):
        if isdecimal(i):
            answer += 1
    
    return answer
"""