'''
import sys

result = ""
c = ord("z") - ord("a") + 1

s = sys.stdin.readline()

for i in s:
    if ord("A") <= ord(i) <= ord("Z"):
        if ord(i) + 13 > ord("Z"):
            result += chr(ord(i) + 13 - c)
        else:
            result += chr(ord(i) + 13)
    elif ord("a") <= ord(i) <= ord("z"):
        if ord(i) + 13 > ord("z"):
            result += chr(ord(i) + 13 - c)
        else:
            result += chr(ord(i) + 13)
    else:
        result += i

print(result)
'''

import sys

s = sys.stdin.readline()
result = []

for i in s:
    if 'A' <= i <= 'Z':
        result.append(chr((ord(i) - ord('A') + 13) % 26 + ord('A')))
    elif 'a' <= i <= 'z':
        result.append(chr((ord(i) - ord('a') + 13) % 26 + ord('a')))
    else:
        result.append(i)

print("".join(result))