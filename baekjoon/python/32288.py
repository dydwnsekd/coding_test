import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

print(s.replace("l", "L").replace("I", "i"))
