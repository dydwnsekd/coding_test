import sys
from re import split

s = "baby sukhwan tururu turu very cute tururu turu in bed tururu turu baby sukhwan"
word_count = len(s.split())

n = int(sys.stdin.readline()) - 1
quotient = n // word_count
remainder = n % word_count

split_s = s.split()

if remainder in [2, 6, 10]:
    return_s = "tu" + "ru" * (quotient + 2)
elif remainder in [3, 7, 11]:
    return_s = "tu" + "ru" * (quotient + 1)
else:
    return_s = split_s[remainder]

if return_s.count("ru") >= 5:
    print(f"tu+ru*{return_s.count('ru')}")
else:
    print(return_s)


