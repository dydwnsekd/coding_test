def solution(n, arr1, arr2):
    """
    1. 10진수 -> 2진수로 변환
    2. 2진수로 변환된 수를 이용해 or 연산으로 하나의 수로 합침
    3. 1 => "#", 0 => ""으로 변경
    """
    answer = []

    binary1 = []
    binary2 = []

    for i in range(n):
        binary1.append(bin(arr1[i])[2:].zfill(n))
        binary2.append(bin(arr2[i])[2:].zfill(n))

    for i in range(n):
        temp_answer = ""
        for j in range(n):
            if binary1[i][j] == "1" or binary2[i][j] == "1":
                temp_answer += "#"
            else:
                temp_answer += " "
        answer.append(temp_answer)

    return answer
