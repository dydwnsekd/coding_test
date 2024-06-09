import sys

n = int(sys.stdin.readline())

for _ in range(n):
    s = sys.stdin.readline().strip()

    result_text = ""
    prev_char = s[0]
    char_count = 0

    for i in s:
        if prev_char == i:
            char_count += 1
        else:
            result_text += f"{str(char_count)} {prev_char} "
            char_count = 1
            prev_char = i

    result_text += f"{str(char_count)} {i} "
    char_count = 1
    prev_char = i

    print(result_text)


