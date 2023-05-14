import sys

person_count = int(sys.stdin.readline())
releation = int(sys.stdin.readline())

result = []
friend = {}
temp = []

for i in range(person_count):
    friend[i+1] = []

for _ in range(releation):
    a, b = map(int, sys.stdin.readline().split())

    if a == 1:
        temp.append(b)
    else:
        friend[a].append(b)
        friend[b].append(a)


result = temp.copy()
for i in temp:
    result.extend(friend[i])

print(len(set(result)))
