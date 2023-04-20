import sys

def get_reverse_alphabet(alphabet):
    alphabet_list = list("-abcdefghijklmnopqrstuvwxyz")
    alphabet_len = len(alphabet_list)
    alphabet_index = alphabet_list.index(alphabet)
    if alphabet_index < 14:
        return alphabet_list[-alphabet_index]
    else:
        return alphabet_list[alphabet_len-alphabet_index]

cases = int(sys.stdin.readline())

for _ in range(cases):
    flag = True
    reverse_word = ""
    word = sys.stdin.readline().strip().lower()

    for w in word:
        if get_reverse_alphabet(w) not in word:
            flag = False
            break

    if flag:
        print("Yes")
    else:
        print("No")
