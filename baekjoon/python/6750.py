import sys

flag = True
rotating_letters = ["I", "O", "S", "H", "Z", "X", "N"]

s = sys.stdin.readline().strip()

for i in s:
    if i not in rotating_letters:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")
