import sys
import string

while True:
    alphabet_dict = {ch: 0 for ch in string.ascii_lowercase}
    s = sys.stdin.readline().strip()

    if s == "*":
        break

    for ch in s:
        alphabet_dict[ch] += 1

    if all(alphabet_dict[ch] for ch in string.ascii_lowercase):
        print("Y")
    else:
        print("N")
