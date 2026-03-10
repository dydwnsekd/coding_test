import sys

reg_user = []
door_status = "close"

n = int(sys.stdin.readline())
for _ in range(n):
    reg_user.append(sys.stdin.readline().strip())

m = int(sys.stdin.readline())
for _ in range(m):
    user = sys.stdin.readline().strip()
    if user in reg_user:
        if door_status == "open":
            print(f"Closed by {user}")
            door_status = "close"
        elif door_status == "close":
            print(f"Opened by {user}")
            door_status = "open"
    else:
        print(f"Unknown {user}")

