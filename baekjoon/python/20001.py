import sys

start_text = sys.stdin.readline().rstrip()
count = 0

if start_text == "고무오리 디버깅 시작":
    while(True):
        text = sys.stdin.readline().rstrip()
        if text == "문제":
            count += 1
        elif text == "고무오리" and count <= 0:
            count += 2
        elif text == "고무오리":
            count -= 1
        elif text == "고무오리 디버깅 끝":
            if count == 0:
                print("고무오리야 사랑해")
                break
            else:
                print("힝구")
                break