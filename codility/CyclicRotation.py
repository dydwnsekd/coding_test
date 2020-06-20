# https://app.codility.com/demo/results/training2FDYM4-ZP3/

'''
def solution(A, K):
    # write your code in Python 3.6
    K = K % len(A)
    
    return A[len(A)-K:] + A[:len(A)-K]
'''

# https://app.codility.com/demo/results/trainingSYVZ6G-TXB/
def solution(A, K):
    # write your code in Python 3.6
    
    if A:
        K = K % len(A)
        return A[len(A)-K:] + A[:len(A)-K]
    else:
        return []