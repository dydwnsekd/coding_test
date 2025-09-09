import sys

n = int(sys.stdin.readline())
items = []

for _ in range(n):
    items.append(int(sys.stdin.readline().strip()))

if "keys" not in items:
    print("keys")
if "phone" not in items:
    print("phone")
if "wallet" not in items:
    print("wallet")
