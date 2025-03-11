import sys

t = int(sys.stdin.readline())

for i in range(t):
    s = sys.stdin.readline().strip()

    print(min(s.count("a"), s.count("b")))

