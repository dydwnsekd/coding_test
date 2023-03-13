import sys
from collections import defaultdict

case_count = 1

while True:
    flag = True
    word_dict = defaultdict(int)
    piece_dict = defaultdict(int)
    word = sys.stdin.readline().strip()
    piece = sys.stdin.readline().strip()

    if word == "END" and piece == "END":
        break

    if len(word) == len(piece):
        for w in word:
            word_dict[w] += 1
        for w in piece:
            piece_dict[w] += 1

        for k in word_dict.keys():
            if word_dict[k] != piece_dict[k]:
                flag = False
                break

    else:
        flag = False

    if flag:
        print(f"Case {case_count}: same")
    else:
        print(f"Case {case_count}: different")

    case_count += 1

