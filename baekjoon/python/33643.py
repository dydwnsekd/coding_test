"""
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
"""

import sys

n = int(sys.stdin.readline())
items = [sys.stdin.readline().strip() for _ in range(n)]

required = ["keys", "phone", "wallet"]

missing = [r for r in required if r not in items]

if not missing:
    print("ready")
else:
    for r in missing:
        print(r)

