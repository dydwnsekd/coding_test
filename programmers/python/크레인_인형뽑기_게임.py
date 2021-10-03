# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    
    bag = [0]
    
    for i in moves:
        j = 0
        while j < len(board):
            
            if board[j][i-1] != 0:
                if board[j][i-1] == bag[-1]:
                    bag.pop()
                    answer += 2
                else:
                    bag.append(board[j][i-1])
                board[j][i-1] = 0
                break
            
            j += 1
    return answer