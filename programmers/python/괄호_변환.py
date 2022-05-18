def solution(p):
    """
    1. 균형잡힌 괄호인지 판별
        - ( 갯수와 ) 갯수를 비교 둘이 같다면 균형잡힌 괄호
    2. 올바른 괄호 문자열인지 판별
        - 균형잡힌 괄호일 때만 올바른 괄호가 될 수 있음
        - 반복문을 이용하여 ( 가 나올 시 +1, ) 가 나올시 -1 하는 과정을 통해 음수가 되거나 반복문 종료 후 0이 아니면 균형잡힌 괄호가 아님
    3. 균형잡힌 괄호지만 올바른 괄호가 아닌 경우 문제에 나와있는 조건에 따라 올바른 괄호로 변경
    """
    balance_flag = False
    correct_flag = True

    left_count = p.count("(")
    right_count = p.count(")")

    if left_count == right_count:
        balance_flag = True

    temp_count = 0
    for i in p:
        if i == "(":
            temp_count += 1
        else:
            temp_count -= 1

        if temp_count < 0:
            correct_flag = False

    if temp_count != 0:
        correct_flag = False

    print(balance_flag)
    print(correct_flag)

if __name__ == "__main__":
    solution(")(")