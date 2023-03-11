import sys

case_count = 1

while True:
    flag = True
    word = sys.stdin.readline().strip()
    piece = sys.stdin.readline().strip()

    if word == "END" and piece == "END":
        break

    # print(word)
    # print(len(word))
    # print(piece)
    # print(len(piece))
    if len(word) == len(piece):
        for w in word:
            if w not in piece:
                flag = False
                break

    if flag:
        print(f"Case {case_count}: same")
    else:
        print(f"Case {case_count}: different")

    case_count += 1

