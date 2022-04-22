def solution(prices):
    answer =[0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i]+=1
            else:
                answer[i]+=1
                break
    return answer

"""
# stack 이용 형식
# stack를 사용할 수 있는 이유
# 가장 최근의 값과 현재 값을 비교하는데 stack의 가장 마지막 값은 로직 상 stack의 어떤 값보다 크거나 같음을 의미
# 따라서 최근 값과 현재 값을 비교 한 후 stack의 나머지 값을 비교함으로써 가격이 떨어지지 않은채 얼마나 유지되고 있는지를 파악할 수 있음
def solution(prices):
    answer = [0]*len(prices)
    stack = []
 
    for i, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
 
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j
 
    return answer
"""