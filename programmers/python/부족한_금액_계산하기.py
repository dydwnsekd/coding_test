# https://programmers.co.kr/learn/courses/30/lessons/82612?language=python3
def solution(price, money, count):
    need_money = 0
    
    for i in range(1, count+1):
        need_money += i*price
        
    if need_money <= money:
        return 0
    else:
        return need_money - money
    