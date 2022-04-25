def solution(N, stages):
    answer = []
    try_counter = [0] * (N + 1)
    failure_rate = [0] * N
    
    for stage in stages:
        for i in range(stage):
            try_counter[i] += 1
            
    for i in range(len(try_counter)-1):
        if try_counter[i] == 0:
            failure_rate[i] = 0.0
        else:
            failure_rate[i] = stages.count(i+1) / float(try_counter[i])
    print(try_counter)
    print(failure_rate)

    return answer