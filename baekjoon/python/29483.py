import sys

result = 0

s = sys.stdin.readline().strip()
atom_dict = {"H": 1, "C": 12, "N": 14, "O": 16}

for i in range(len(s)):
    if s[i] in atom_dict.keys():
        if s[i+1] not in atom_dict.keys():
            result += int(s[i+1]) * atom_dict[s[i]]
        else:
            result += atom_dict[s[i]]

print(result)
