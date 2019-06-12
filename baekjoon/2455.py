import sys

p = 0 
max_person = -1

for _ in range(4):
    out_person, in_person = list(map(int, sys.stdin.readline().split(" ")))
    p -= out_person
    p += in_person

    if max_person < p:
        max_person = p

print (max_person)
