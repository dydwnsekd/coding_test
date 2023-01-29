import sys

cases = int(sys.stdin.readline())
for _ in range(cases):
    word_count = int(sys.stdin.readline())
    for _ in range(word_count):
        word = sys.stdin.readline().strip()
        split_word = word.split()

        englist_index = -1

        for i in range(len(split_word)):
            if not split_word[i].startswith("#"):
                englist_index = i
                break

        if englist_index == -1:
            print(word)
        else:
            result = [word[englist_index+1:]]
            result.append(word[englist_index])
            result.append(word[:englist_index])
            print(" ".join(result))


