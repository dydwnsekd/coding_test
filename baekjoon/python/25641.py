import sys

length = int(sys.stdin.readline())
s = sys.stdin.readline()

while True:
    if s.count("s") == s.count("t"):
        break
    else:
        s = s[1:]

print(s)
