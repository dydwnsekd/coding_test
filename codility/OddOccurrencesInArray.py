# https://app.codility.com/demo/results/trainingMUNEKX-RNN/

def solution(A):
    # write your code in Python 3.6
    
    result_list = []
    for i in A:
        if i in result_list:
            result_list.remove(i)
        else:
            result_list.append(i)
        
    return result_list[0]