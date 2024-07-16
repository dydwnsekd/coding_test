import sys

vowels = ["a", "e", "i", "o", "u"]
count = 0
y_count = 0

s = sys.stdin.readline().strip()

for i in s:
    if i in vowels:
        count += 1
    if i == "y":
        y_count += 1

print(f"{count} {count + y_count}")
