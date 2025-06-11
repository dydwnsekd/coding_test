import sys

t = int(sys.stdin.readline())

for _ in range(t):
    plain_keyword, plaintext = sys.stdin.readline().split()
    keyword = ""
    result = ""

    while len(plaintext) > len(keyword):
        keyword += plain_keyword

    keyword = keyword[:len(plaintext)]

    for i in range(len(plaintext)):
        result += chr((ord(plaintext[i]) + ord(keyword[i]) - ord("A") - ord("A") ) % 26 + ord("A"))

    print("Ciphertext:", result)