# https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3
from collections import Counter

def solution(participant, completion):    
    count_participant = Counter(participant)
    count_completion = Counter(completion)

    for k in count_participant.keys():
        if count_participant[k] != count_completion[k]:
            return k