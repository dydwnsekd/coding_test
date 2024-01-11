import sys

vowels = ["a", "e", "i", "o", "u"]
cases = int(sys.stdin.readline())

for _ in range(cases):
    s = sys.stdin.readline().strip()
    count = 0
    for i in s:
        if i in vowels:
            count += 1

    print(f"The number of vowels in {s} is {count}.")
