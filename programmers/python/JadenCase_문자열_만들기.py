# https://programmers.co.kr/learn/courses/30/lessons/12951#
def solution(s):
    answer = ''
    pre_string = " "
    s = s.lower()
    
    for i in range(len(s)):
        if pre_string == " ":
            answer += s[i].upper()
        else:
            answer += s[i]
        pre_string = s[i]
    
    return answer