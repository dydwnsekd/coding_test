# https://programmers.co.kr/learn/courses/30/lessons/87389?language=python3
def solution(n):
    answer = 0
    
    for i in range (2,n):
        if n % i == 1:
            return i