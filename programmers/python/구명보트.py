# https://programmers.co.kr/learn/courses/30/lessons/42885?language=python3
# 효율성 테스트 1 시간 초과 실패
def solution(people, limit):
    answer = 0
    people.sort()
    
    while len(people) > 0:
        answer += 1
        temp = people.pop()
        if len(people) > 0 and temp + people[0] <= limit:
            people.pop(0)   

    return answer