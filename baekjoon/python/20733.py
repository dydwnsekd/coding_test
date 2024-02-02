import sys

s = sys.stdin.readline().strip()
len_s = len(s) // 3

s1 = s[:len_s]
s2 = s[len_s:len_s*2]
s3 = s[len_s*2:len_s*3]

if s1 == s2 or s1 == s3:
    print(s1)
else:
    print(s2)
