from itertools import combinations

def is_decimal(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

def solution(nums):
    answer = 0
    
    number_of_cases = list(combinations(nums, 3))
    for i in number_of_cases:
        if is_decimal(sum(i)):
            answer += 1

    return answer