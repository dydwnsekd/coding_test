# https://programmers.co.kr/learn/courses/30/lessons/42626
def solution(scoville, K):
    answer = 0
    
    while True:
        scoville.sort()
        if scoville[0] >= K:
            return answer
        else:
            answer += 1
            scoville.append(scoville.pop(1) * 2 + scoville.pop(0))
    
    return answer