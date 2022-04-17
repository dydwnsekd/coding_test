def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        temp = 0
        for j in prices[i:]:
            if prices[i] <= j:
                temp += 1
            else:
                break
        answer.append(temp)
        print(temp)
    
    return answer