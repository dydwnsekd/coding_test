def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        temp = 0
        for j in prices[i+1:]:
            if prices[i] <= j:
                temp += 1
            else:
                break
        answer.append(temp)
    
    for i in range(len(answer)-1):
        if answer[i] == 0:
            answer[i] = 1
    
    return answer