import sys

s = "baby sukhwan tururu turu very cute tururu turu in bed tururu turu baby sukhwan"
word_count = len(s.split()) + 1

n = int(sys.stdin.readline())
quotient = n // word_count
remainder = n % word_count

print(word_count, quotient, remainder)

for _ in range(quotient):
    s = s.replace("turu", "tururu")

split_s = s.split()

print(split_s[remainder])

