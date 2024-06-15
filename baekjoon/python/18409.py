import sys

count = 0

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

vowel_list = ['a', 'i', 'u', 'e', 'o']

for i in s:
    if i in vowel_list:
        count += 1

print(count)
