# https://programmers.co.kr/learn/courses/30/lessons/12951#
def solution(s):
    answer = ''
    
    for i in s.split():
            answer = answer + i[0].upper() + i[1:].lower() + ' '
    
    return answer[:-1]