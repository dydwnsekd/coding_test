def divide_uv(p):
    left_count = 0
    right_count = 0

    for i in range(len(p)):
        if p[i] == '(':
            left_count += 1
        else:
            right_count += 1

        if left_count == right_count:
            return p[:i+1], p[i+1:]


def is_right_bracket(bracket):
    temp_count = 0
    for i in bracket:
        if i == "(":
            temp_count += 1
        else:
            temp_count -= 1

        if temp_count < 0:
            return False

    if temp_count != 0:
        return False

    return True


def sol(p):
    result = ""

    if len(p) == 0:
        return ""

    u, v = divide_uv(p)
    if is_right_bracket(u):
        result = u + solution(v)
    else:
        temp = "("
        temp += solution(v)
        temp += ")"
        for t in u[1:-1]:
            if t == "(":
                temp += ")"
            else:
                temp += "("
        result += temp

    return result


def solution(p):
    """
    1. 균형잡힌 괄호인지 판별
        - ( 갯수와 ) 갯수를 비교 둘이 같다면 균형잡힌 괄호 -> 항상 균형잡힌 문자열이 입력되므로 확인할 필요 없음
    2. 올바른 괄호 문자열인지 판별
        - 균형잡힌 괄호일 때만 올바른 괄호가 될 수 있음
        - 반복문을 이용하여 ( 가 나올 시 +1, ) 가 나올시 -1 하는 과정을 통해 음수가 되거나 반복문 종료 후 0이 아니면 균형잡힌 괄호가 아님
    3. 균형잡힌 괄호지만 올바른 괄호가 아닌 경우 문제에 나와있는 조건에 따라 올바른 괄호로 변경
        - 괄호 문자열을 u, v 로 분리
        - 각 괄호 문자열에 대해 올바른 괄호 문자열인지 판별
        - 문제에서 제시한 방법을 통해 재귀적으로 올바른 괄호 문자열로 변경
    """

    return sol(p)


if __name__ == "__main__":
    print(solution(")("))
