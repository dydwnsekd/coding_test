import sys

result = ""

s = sys.stdin.readline().strip()

alphabet_list = s[:3]
num_list = s[3:]

alphabet_list = sorted(alphabet_list)
num_list = sorted(num_list, reverse=True)

for i in range(3):
    result += alphabet_list[i] + num_list[i]

print(result)

