"""
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
"""

import sys

n, m = map(int, sys.stdin.readline().split())
output_lines = []

for _ in range(n):
    s = sys.stdin.readline().strip()
    half = m // 2
    first_half = s[:half]
    second_half = s[half:][::-1]

    merged_half = ''.join(
        second_half[i] if first_half[i] == '.' else first_half[i]
        for i in range(half)
    )

    full_line = merged_half + merged_half[::-1]
    output_lines.append(full_line)

print('\n'.join(output_lines))

