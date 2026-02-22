import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

while n < 0:
    n -= 1
    result = ""
    num_count = 0

    for i in range(len(s)):
        if s[i] == s[i+1]:
            num_count += 1
        else:
            result += f"{num_count}{s[i]}"
            num_count = 0

        print(num_count)

    s = result

print(s)
