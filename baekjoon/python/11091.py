"""
import sys

alphabet_list = list("abcdefghijklmnopqrstuvwxyz")
alphabet_dict = {}

n = int(sys.stdin.readline())

for i in range(n):
    no_alphabet = []

    for alphabet in alphabet_list:
        alphabet_dict[alphabet] = False

    s = sys.stdin.readline().strip().lower()

    for j in s:
        if j in alphabet_dict.keys():
            alphabet_dict[j] = True

    for key in alphabet_dict.keys():
        if not alphabet_dict[key]:
            no_alphabet.append(key)

    if len(no_alphabet) == 0:
        print("pangram")
    else:
        no_alphabet = sorted(no_alphabet)
        print(f"missing {''.join(no_alphabet)}")
"""

import sys

alphabet_list = set("abcdefghijklmnopqrstuvwxyz")

n = int(sys.stdin.readline())

for i in range(n):
    input_set = set(sys.stdin.readline().strip().lower())

    missing_alphabet = alphabet_list - input_set

    if not missing_alphabet:
        print("pangram")
    else:
        print(f"missing {''.join(sorted(missing_alphabet))}")
