import sys

Vowel_list = ["a", "e", "i", "o", "u"]
result = 0
s = list(sys.stdin.readline().strip())

for i in s:
    if i in Vowel_list:
        result += 1

print(result)
