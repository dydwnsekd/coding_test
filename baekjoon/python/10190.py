import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    match_text, temp_case = sys.stdin.readline().split()
    temp_case = int(temp_case)

    for _ in range(temp_case):
        text = sys.stdin.readline().replace("\n", "")
        print("".join(text.split(" ")))
