# https://app.codility.com/demo/results/trainingMUNEKX-RNN/
# 시간 초과
def solution(A):
    # write your code in Python 3.6
    
    result_list = []
    for i in A:
        if i in result_list:
            result_list.remove(i)
        else:
            result_list.append(i)
        
    return result_list[0]

# https://app.codility.com/demo/results/trainingMTFFB9-Q8F/
# 시간 초과
def solution(A):
    while(A):
        temp = A.pop(0)
        if temp in A:
            A.remove(temp)
        else:
            return_value = temp
            break
    return return_value

# https://app.codility.com/demo/results/training63NDEX-CW7/
# 정확도, 시간초과 문제

def solution(A):
    B = set(A)
    
    for i in B:
        if A.count(i) == 1:
            return i