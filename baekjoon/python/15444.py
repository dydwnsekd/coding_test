"""
import sys

lines = ["", "", "", "", ""]

line_ch = [
    ["***", "*.*", "***", "*.*", "*.*"],
    ["***", "*.*", "***", "*.*", "***"],
    ["***", "*..", "*..", "*..", "***"],
    ["***", "*.*", "*.*", "*.*", "***"],
    ["***", "*..", "***", "*..", "***"]
]

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

for c in s:
    ch = ord(c) - ord('A')

    for i in range(5):
        lines[i] += line_ch[ch][i]

for i in range(5):
    print(''.join(lines[i]))
"""

import sys

letter_patterns = {
    'A': ["***", "*.*", "***", "*.*", "*.*"],
    'B': ["***", "*.*", "***", "*.*", "***"],
    'C': ["***", "*..", "*..", "*..", "***"],
    'D': ["***", "*.*", "*.*", "*.*", "***"],
    'E': ["***", "*..", "***", "*..", "***"]
}

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

lines = [[] for _ in range(5)]

for ch in s:
    pattern = letter_patterns.get(ch, ["...", "...", "...", "...", "..."])  # 에러 방지 기본값
    for i in range(5):
        lines[i].append(pattern[i])

for line in lines:
    print(''.join(line))

