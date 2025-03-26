import sys

for _ in range(15):
    s = sys.stdin.readline().strip().replace(' ', '')

    if "w" in s:
        print("chunbae")
        break
    elif "b" in s:
        print("nabi")
        break
    elif "g" in s:
        print("yeongcheol")
        break

