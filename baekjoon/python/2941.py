import sys

text = sys.stdin.readline()

croatia_text = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
count = 0

for i in croatia_text:
    count += text.count(i)
    text = text.replace(i, "&")

text = text.replace("&", "")
print(count + len(text)-1)