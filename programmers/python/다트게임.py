import re


def solution(dartResult):
    """
    1. 점수/보너스/옵션 형식의 input 나누기 (옵션은 존재하지 않을 수도 있음)
    2. 점수 + 보너스, 점수 + 보너스 + 옵션 계산식 산출
    3. 계산 점수 return
    """

    answer = 0

    score_pattern = re.compile("[1-9][S|D|T][*|#]*")
    score_list = score_pattern.findall(dartResult)

    for i in score_list:
        print(i)

    return answer


if __name__ == "__main__":
    test_list = ["1S2D*3T", "1D2S#10S", "1D2S0T", "1S*2T*3S", "1D#2S*3S", "1T2D3D#", "1D2S3T*"]

    for test in test_list:
        solution(test)
        print("------------------------")
