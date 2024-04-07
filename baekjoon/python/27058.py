import sys

result = ""
secret_dict = {}
upper_lower = ord("a") - ord("A")
alphabet_index = ord("a")
secrets = sys.stdin.readline().strip()

for i in secrets:
    secret_dict[alphabet_index] = i
    secret_dict[alphabet_index - upper_lower] = chr(ord(i) - upper_lower)
    alphabet_index += 1

s = sys.stdin.readline().strip()

for i in s:
    if i == " ":
        result += " "
    else:
        result += secret_dict[ord(i)]

print(result)
