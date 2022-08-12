import sys

n = int(sys.stdin.readline())
word_list = []
for _ in range(n):
    word_list.append(sys.stdin.readline().strip())

word_list = list(set(word_list))
word_list = sorted(word_list, key=lambda word_list: [len(word_list), word_list])

for word in word_list:
    print(word)
