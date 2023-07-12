import sys

start_char = sys.stdin.readline().strip()
min_distance = 84
criteria = "I"

min_distance += abs(ord(start_char) - ord(criteria))

print(min_distance)
