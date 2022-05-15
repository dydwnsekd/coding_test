def solution(s):
    """
    1. input이 문자열이기 때문에 문자열을 list 혹은 튜플로 변경 (o)
    2. sorted(a, key=lambda a: len(a))를 이용해 문자열 길이로 정렬 (o)
    3. 정렬된 문자열을 이용하여 튜플 완성
    """
    s = s.replace("{", "[").replace("}", "]")
    list_s = eval(s)
    print(list_s)

    list_s = sorted(list_s, key=lambda s: len(s))
    print(list_s)

if "__main__" == __name__:
    s = "{{1,2,3,4}, {2}, {2,3,1}, {1,2}}"
    solution(s)