import sys

prev_len = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

while True:
    s = s.replace("PS4", "PS").replace("PS5", "PS")

    if len(s) == prev_len:
        break
    else:
        prev_len = len(s)

print(s)
