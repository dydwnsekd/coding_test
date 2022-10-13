import sys

while True:
    s = sys.stdin.readline().strip()

    if s == "#":
        break
    else:
        if s[-1] == "e":
            if s.count("1") % 2 == 0:
                print(s[:-1] + "0")
            else:
                print(s[:-1] + "1")
        else:
            if s.count("1") % 2 == 0:
                print(s[:-1] + "0")
            else:
                print(s[:-1] + "1")
