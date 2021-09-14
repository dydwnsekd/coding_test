# https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3
def solution(participant, completion):    
    for i in participant:
        if i not in completion:
            return i
        else:
            completion.remove(i)