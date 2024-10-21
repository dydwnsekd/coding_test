import sys

s = "baby sukhwan tururu turu very cute tururu turu in bed tururu turu baby sukhwan"
word_count = len(s.split())

n = int(sys.stdin.readline()) - 1
quotient = n // word_count
remainder = n % word_count

for _ in range(quotient):
    s = s.replace("turu", "tururu")

split_s = s.split()

if split_s[remainder].count("ru") >= 5:
    print(f"tu+ru*{split_s[remainder].count('ru')}")
else:
    print(split_s[remainder])


