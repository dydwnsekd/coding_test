import sys

type_text = \
    [
        ["1", "Q", "A", "Z"],
        ["2", "W", "S", "X"],
        ["3", "E", "D", "C"],
        ["4", "R", "F", "V", "5", "T", "G", "B"],
        ["6", "Y", "H", "N", "7", "U", "J", "M"],
        ["8", "I", "K", ","],
        ["9", "O", "L", "."],
        ["0", "P", ";", "/", "-", "[", "'", "=", "]"]
    ]

finger_count = [0, 0, 0, 0, 0, 0, 0, 0]

s = sys.stdin.readline().strip()

for c in s:
    for i in range(len(type_text)):
        if c == type_text[i]:
            finger_count[i] += 1

for i in range(len(finger_count)):
    print(finger_count[i])

