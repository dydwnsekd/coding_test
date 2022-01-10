import re

def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    for i in new_id:
        if ord(i) in range(97, 123):
            answer += i
        elif i in ["-","_","."]:
            answer += i
    
    # 3단계
    answer = re.sub("\.+", ".", answer)
    
    # 4단계
    if answer[0] == ".":
        answer = answer[1:]
    if answer[-1] == ".":
        answer = answer[:-1]
    
    # 5단계
    if answer == "":
        answer = "a"
    
    # 6단계
    if len(answer) > 15:
        answer = answer[:15]
    if answer[-1] == ".":
        answer = answer[:-1]
    
    # 7단계
    while len(answer) < 3:
        answer += answer[-1]
    
    return answer