def solution(N, stages):
    answer = []

    for i in range(1, N + 1):
        fail_count = 0
        try_count = 0
        for j in stages:
            if i == j:
                fail_count += 1
                try_count += 1
            elif j > i:
                try_count += 1

        if try_count == 0:
            answer.append(1)
        else:
            answer.append(float(fail_count) / try_count)
        print(i)
        print(fail_count)
        print(try_count)
        print("===================")

    return answer