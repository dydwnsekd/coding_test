def solution(answers):
    p_1 = [1,2,3,4,5]
    p_2 = [2,1,2,3,2,4,2,5]
    p_3 = [3,3,1,1,2,2,4,4,5,5]
    
    result = [0,0,0]
    count = 0
    
    for i in answers:
        if i == p_1[count%len(p_1)]:
            result[0] = result[0] + 1
        if i == p_2[count%len(p_2)]:
            result[1] = result[1] + 1
        if i == p_2[count%len(p_3)]:
            result[2] = result[2] + 1
        count += 1
        
    if min(result) == max(result):
        return [1,2,3]
    
    return result(index(max(result)))