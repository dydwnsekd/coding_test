import sys, operator

t = sys.stdin.readline().strip()
s = "CHICKENS"

key = operator.xor(ord(t[0]), ord(s[0]))
result = ""

for i in t:
    result += chr(operator.xor(ord(i), key))

print(result)

