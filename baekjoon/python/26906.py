import sys

alphabet_dict = {}
result = ""
cases = int(sys.stdin.readline())

for _ in range(cases):
    alphabet, binary_code = sys.stdin.readline().split()
    alphabet_dict[alphabet] = binary_code

s = sys.stdin.readline().strip()

for i in range(0, len(s)-1, 4):
    if s[i:i+4] in alphabet_dict.keys():
        result += alphabet_dict[s[i:i+4]]
    else:
        result += "?"

print(result)
