def decimal_to_binary(decimal_number):
    binary_num = ""
    if decimal_number == 0:
        return "0"
    while decimal_number > 0:
        binary_num = str(decimal_number % 2) + binary_num
        decimal_number = decimal_number // 2

    return binary_num

def solution(n, arr1, arr2):
    """
    1. 10진수 -> 2진수로 변환
    2. 2진수로 변환된 수를 이용해 or 연산으로 하나의 수로 합침
    3. 1 => "#", 0 => ""으로 변경
    """
    answer = []

    binary1 = []
    binary2 = []

    for i in arr1:
        print(decimal_to_binary(i))


    return answer


if __name__ == "__main__":
    solution(0, [9, 20, 28, 18, 11], [])
