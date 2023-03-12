import sys

case_count = 1

while True:
    flag = True
    word = sys.stdin.readline().strip()
    piece = sys.stdin.readline().strip()

    if word == "END" and piece == "END":
        break

    if len(word) == len(piece):
        for w in word:
            if w not in piece:
                flag = False
                break
            else:
                del_index = piece.find(w)
                del piece[del_index]
    else:
        flag = False

    if flag:
        print(f"Case {case_count}: same")
    else:
        print(f"Case {case_count}: different")

    case_count += 1

