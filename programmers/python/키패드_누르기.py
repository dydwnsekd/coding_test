def solution(numbers, hand):
    answer = ""
    distance = [[1,3],[0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2],[0,3],[2,3]]
    L = 10
    R = 11
    
    L_location = [1,4,7]
    R_location = [3,6,9]
    
    for i in numbers:
        if i in L_location:
            answer += "L"
            L = i
        elif i in R_location:
            answer += "R"
            R = i
        else:
            L_distance = abs(distance[i][0] - distance[L][0]) + abs(distance[i][1] - distance[L][1])
            R_distance = abs(distance[i][0] - distance[R][0]) + abs(distance[i][1] - distance[R][1])

            if L_distance > R_distance:
                answer += "R"
                R = i
            elif L_distance < R_distance:
                answer += "L"
                L = i
            else:
                if hand == "right":
                    answer += "R"
                    R = i
                else:
                    answer += "L"
                    L = i

    return answer