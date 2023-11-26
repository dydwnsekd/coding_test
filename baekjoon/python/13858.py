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
s_1 = bobs_encoding(s)
s_2 = bobs_encoding(s_1)

print(s_2[pos+1])

