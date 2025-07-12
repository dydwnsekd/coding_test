import sys

output_line = ""
n, m = map(int, sys.stdin.readline().strip().split())

for _ in range(n):
    temp_s = ""

    s = sys.stdin.readline().strip()

    first_s = s[:m//2]
    second_s = s[m//2:][::-1]

    for i in range(m//2):
        if first_s[i] == ".":
            temp_s += second_s[i]
        else:
            temp_s += first_s[i]

        output_line += temp_s + temp_s[::-1] + "\n"


    print(output_line)

