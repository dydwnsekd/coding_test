def solution(n):
    answer = ''
    num_124 = ['1','2','4']
    
    """
    로직 변경 필요
    10진수    답    현재 로직
    1         1     1
    2         2     2
    3         4     4
    4         11     11
    5         12     21
    6         14     42
    7         21     12
    8         22     22
    9         24     44
    10        41     14
    11        42     24
    12        44     141
    """
    while True:
        if n > 3:
            answer = num_124[(n%3)-1] + answer
            n = n//3
        else:
            answer += num_124[n-1]
            break
    
    return answer