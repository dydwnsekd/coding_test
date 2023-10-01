import sys

result = ""
mbti = sys.stdin.readline().strip()

if mbti[0] == "E":
    result += "I"
else:
    result += "E"

if mbti[1] == "S":
    result += "N"
else:
    result += "S"

if mbti[2] == "T":
    result += "F"
else:
    result += "T"

if mbti[3] == "J":
    result += "P"
else:
    result += "J"

print(result)





