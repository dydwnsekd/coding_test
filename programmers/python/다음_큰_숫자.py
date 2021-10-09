# https://programmers.co.kr/learn/courses/30/lessons/12911?language=python3

def solution(n):
    count1 = bin(n).count('1')
    
    while True:
        n += 1
        if count1 == bin(n).count('1'):
            break
    
    return n