import sys

long_string = sys.stdin.readline().strip()
short_string = ""
word_list = long_string.split("-")

for w in word_list:
    short_string += w[0]

print(short_string)
