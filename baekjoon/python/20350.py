import sys

s = sys.stdin.readline().strip()
s = s[4:] + s[:4]
change_s = ""

for i in s:
    if ord("A") <= ord(i) <= ord("Z"):
        change_s += str(ord(i) - 55)
    else:
        change_s += i

if int(change_s) % 97 == 1:
    print("correct")
else:
    print("incorrect")


