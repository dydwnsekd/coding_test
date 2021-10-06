# https://programmers.co.kr/learn/courses/30/lessons/83201?language=python3
def solution(scores):
    answer = ''
    student_score = [ [] for _ in range(len(scores))]
    
    for i in range(len(scores)):
        for j in range(len(scores)):
            student_score[i].append(scores[j][i])
            
    for i in range(len(scores)):
        if student_score[i][i] == min(student_score[i]) or student_score[i][i] == max(student_score[i]):
            student_score[i].pop(i)
            
        avg_score = sum(student_score[i])//len(student_score[i])
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