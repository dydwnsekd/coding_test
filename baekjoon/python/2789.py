import sys

DELETE_ALPHABET = "CAMBRIDGE"
word = sys.stdin.readline()

for i in DELETE_ALPHABET:
    word = word.replace(i, "")

print(word)
