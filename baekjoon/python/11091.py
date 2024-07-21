import sys

alphabet_list = list("abcdefghijklmnopqrstuvwxyz")
alphabet_dict = {}

n = int(sys.stdin.readline())

for i in range(n):
    no_alphabet = []

    for alphabet in alphabet_list:
        alphabet_dict[alphabet] = False

    s = sys.stdin.readline().strip().lower()

    for j in s:
        if j in alphabet_dict.keys():
            alphabet_dict[j] = True

    for key in alphabet_dict.keys():
        if not alphabet_dict[key]:
            no_alphabet.append(key)

    if len(no_alphabet) == 0:
        print("pangram")
    else:
        no_alphabet = sorted(no_alphabet)
        print(f"missing {''.join(no_alphabet)}")

