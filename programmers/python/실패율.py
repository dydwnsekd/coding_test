def solution(N, stages):
    answer = []
    try_counter = [0] * (N + 1)
    
    for stage in stages:
        for i in range(stage):
            try_counter[i] += 1
            
    print(try_counter)

    return answer