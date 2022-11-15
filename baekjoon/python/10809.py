import sys

alphabet_list = [-1] * 26

s = sys.stdin.readline().strip()

for i in range(len(s)):
    if alphabet_list[ord(s[i]) - 97] == -1:
        alphabet_list[ord(s[i]) - 97] = i

for i in range(len(alphabet_list)):
    print(alphabet_list[i], end=" ")
