# import sys
#
# result = ""
#
# k = int(sys.stdin.readline())
# s = sys.stdin.readline().strip()
#
# for i in range(len(s)):
#     result += chr(ord("A") + (ord(s[i]) - (3 * (i+1)) - k - ord("A")) % 26)
#
# print(result)

import sys

k = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

base_ord = ord('A')
decoded_chars = []

for idx, ch in enumerate(s):
    offset = (ord(ch) - (3 * (idx + 1)) - k - base_ord) % 26
    decoded_char = chr(base_ord + offset)
    decoded_chars.append(decoded_char)

print(''.join(decoded_chars))

