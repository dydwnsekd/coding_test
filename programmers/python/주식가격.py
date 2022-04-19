def solution(prices):
    answer = []
    last_flag = [True] * len(prices)
    
    for i in range(len(prices)):
        temp = 1
        for j in prices[i+1:]:
            if prices[i] <= j:
                temp += 1
            else:
                last_flag[i] = False
                break
        answer.append(temp)
    
    for i in range(len(last_flag)):
        if last_flag[i]:
            answer[i] = answer[i] - 1
    
    answer[-1] = 0
    
    return answer