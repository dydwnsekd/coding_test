import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    match_text, temp_case = sys.stdin.readline().split()
    temp_case = int(temp_case)
    print(match_text)

    for _ in range(temp_case):
        text = sys.stdin.readline().strip()
        split_text = text.split()

        head_text = ''.join([t[0] for t in split_text])
        if match_text == head_text:
            print(text)
