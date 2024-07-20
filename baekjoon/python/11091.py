import sys

alphabet_list = list("abcdefghijklmnopqrstuvwxyz")
alphabet_dict = {}

n = int(sys.stdin.readline())

for i in range(n):
    for alphabet in alphabet_list:
        alphabet_dict[alphabet] = False

    s = sys.stdin.readline().strip().lower()

    for j in s:
        if j in alphabet_dict.keys():
            alphabet_dict[j] = True

    if all(alphabet for alphabet in alphabet_dict.values()):
        print("pangram")
    else:
        print("missing")


