import sys

def bobs_encoding(s):
    len_s = len(s)
    result = ""

    for i in range(0, len_s-1, 2):
        count = int(s[i])
        num = s[i+1]

        result += num * count

    return result

k, pos = map(int, sys.stdin.readline().split())

s = sys.stdin.readline()

for _ in range(k):
    s = bobs_encoding(s)

print(s[pos+1])

