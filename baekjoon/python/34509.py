# print(42)

result = []

for n in range(10, 100):
    s = str(n)

    if '8' in s:
        continue

    rev = int(s[::-1])

    if rev % 4 != 0:
        continue

    digit_sum = sum(int(ch) for ch in s)
    if digit_sum % 6 != 0:
        continue

    result.append(n)

print(result)