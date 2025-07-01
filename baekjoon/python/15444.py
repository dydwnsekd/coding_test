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

