def solution(s):
    """
    1. input이 문자열이기 때문에 문자열을 list 혹은 튜플로 변경
    2. sorted(a, key=lambda a: len(a))를 이용해 문자열 길이로 정렬
    3. 정렬된 문자열을 이용하여 튜플 완성
    """