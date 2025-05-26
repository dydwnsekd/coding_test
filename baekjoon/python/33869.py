"""
import sys

alphabet_list = []
secret_dict = {}
secret_alphabet = 'A'

for i in range(ord('A'), ord('Z') + 1):
    alphabet_list.append(chr(i))

w = sys.stdin.readline().strip()

for c in w:
    if c in alphabet_list:
        secret_dict[secret_alphabet] = c
        alphabet_list.remove(c)
        secret_alphabet = chr(ord(secret_alphabet) + 1)

for c in alphabet_list:
    secret_dict[secret_alphabet] = c
    secret_alphabet = chr(ord(secret_alphabet) + 1)

s = sys.stdin.readline().strip()
result = ''

for c in s:
    result += secret_dict[c]

print(result)
"""

import sys
import string

w = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()

used = set()
secret_dict = {}

next_key_idx = 0

for c in w:
    if c not in used:
        secret_dict[chr(ord('A') + next_key_idx)] = c
        used.add(c)
        next_key_idx += 1

for c in string.ascii_uppercase:
    if c not in used:
        secret_dict[chr(ord('A') + next_key_idx)] = c
        next_key_idx += 1

result = ''.join(secret_dict[c] for c in s)
print(result)
