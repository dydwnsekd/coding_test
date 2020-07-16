import sys

a, b = list(sys.stdin.readline().split(" "))

max_a = list()
max_b = list()
min_a = list()
min_b = list()

for i in range(len(a)):
    if a[i] == '5' or a[i] == '6':
        max_a.append('6')
        min_a.append('5')
    else:
        max_a.append(a[i])
        min_a.append(a[i])
    
for i in range(len(a)):
    if b[i] == '5' or b[i] == '6':
        max_b.append('6')
        min_b.append('5')
    else:
        max_b.append(b[i])
        min_b.append(b[i])

max_a = int("".join(max_a))
min_a = int("".join(min_a))
max_b = int("".join(max_b))
min_b = int("".join(min_b))

print ("%d %d" % (min_a + min_b, max_a + max_b))

