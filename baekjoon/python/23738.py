import sys

s_dict = {"B": "v", "E": "ye", "H": "n", "P": "r", "C": "s", "Y": "u", "X": "h", "A": "a", "K": "k", "M": "m", "O": "o", "T": "t"}

s = sys.stdin.readline().strip()
result = ""

for i in s:
    if i in s_dict:
        result += s_dict[i]

print(result)
