def solution(numbers, hand):
    answer = ""
    L = "*"
    R = "#"
    
    L_location = [1,4,7]
    R_location = [3,6,9]
    N_location = [2,5,8,0]
    
    for i in numbers:
        if i in L_location:
            answer += "L"
            L = i
        elif i in R_location:
            answer += "R"
            R = i
        else:
            pass