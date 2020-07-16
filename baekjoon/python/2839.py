a = input()

a = int(a)

for i in range(int(a/5), -1, -1):
    share = i
    rest = a - (i * 5)

    if rest != 0 and rest%3 == 0:
        share = share + int(rest/3)
        rest = 0

    if rest == 0:
        break

    share = 0

if share != 0:
    print (share)
else:
    print (-1)
    