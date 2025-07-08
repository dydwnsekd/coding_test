import sys

while True:
    s = sys.stdin.readline().strip()
    total_count = len(s)
    participant_count = 0
    y_count = 0
    n_count = 0

    if s == "#":
        break

    for c in s:
        if c == "Y":
            participant_count += 1
            y_count += 1
        elif c == "N":
            participant_count += 1
            n_count += 1
        elif c == "P":
            participant_count += 1

    if total_count >= participant_count // 2:
        if y_count > n_count:
            print("yes")
        elif y_count < n_count:
            print("no")
        elif y_count == n_count:
            print("tie")
    else:
        print("need quorum")


