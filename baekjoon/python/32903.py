import sys

alphabet_list = ["."] * 26

n = int(sys.stdin.readline())

for _ in range(n):
    s = sys.stdin.readline().strip()[0]
    alphabet_list[ord(s) - ord('a')] = s

for i in range(4):
    print("".join(alphabet_list[6*i:6*i+6]))

