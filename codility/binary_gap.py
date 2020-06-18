# https://app.codility.com/demo/results/trainingTQ9R4G-X74/

def solution(N):
    # write your code in Python 3.6
    binary_num = "{0:b}".format(N)
    count = 0
    temp = 0
    
    for i in binary_num:
        if i == '0':
            temp += 1
        else:
            if count < temp:
                count = temp
            temp = 0
        
    return count