import sys

n = int(sys.stdin.readline())
items = []

for _ in range(n):
    items.append(sys.stdin.readline().strip())

if "keys" in items and "phone" in items and "wallet" in items:
    print("ready")
else:
    if "keys" not in items:
        print("keys")
    if "phone" not in items:
        print("phone")
    if "wallet" not in items:
        print("wallet")
