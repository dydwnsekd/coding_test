import sys

taebo = sys.stdin.readline().strip()
punch = taebo.split("(^0^)")

left = punch[0].count("@")
right = punch[1].count("@")

print(left, right)
