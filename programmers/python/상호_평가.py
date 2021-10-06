# https://programmers.co.kr/learn/courses/30/lessons/83201?language=python3
def solution(scores):
    answer = ''
    ss = [ [] for _ in range(len(scores))]
    
    for i in range(len(scores)):
        for j in range(len(scores)):
            ss[i].append(scores[j][i])
            
    for i in range(len(scores)):
        if (ss[i][i] == min(ss[i]) and ss[i].count(min(ss[i])) == 1) or \
        (ss[i][i] == max(ss[i]) and ss[i].count(max(ss[i])) == 1):
            ss[i].pop(i)
            
        avg_score = sum(ss[i])//len(ss[i])
        if avg_score >= 90:
            answer += "A"
        elif avg_score >= 80:
            answer += "B"
        elif avg_score >= 70:
            answer += "C"
        elif avg_score >= 50:
            answer += "D"
        else:
            answer += "F"

    return answer