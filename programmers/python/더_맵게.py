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

"""
def solution(scoville, K):
    answer = 0
    scoville.sort()
    
    while True:
        if scoville[0] >= K:
            return answer
        else:
            answer += 1
            temp = scoville.pop(1) * 2 + scoville.pop(0)
            # print(scoville)
            # print(temp)
            for i in range(len(scoville)):
                if temp <= scoville[i]:
                    scoville.insert(i, temp)
                    break
                elif i == len(scoville) - 1:
                    scoville.append(temp)
            # print(scoville)
    
    return answer
"""