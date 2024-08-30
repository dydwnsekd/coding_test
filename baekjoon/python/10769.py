import sys

happy_imoji = ":-)"
sad_imoji = ":-("

s = sys.stdin.readline().strip()

happy_count = s.count(happy_imoji)
sad_count = s.count(sad_imoji)

if happy_count == 0 and sad_count == 0:
    print("none")
elif happy_count == sad_count:
    print("unsure")
elif happy_count > sad_count:
    print("happy")
elif happy_count < sad_count:
    print("sad")

