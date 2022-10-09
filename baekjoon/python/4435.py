import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    gandalf_score_list = [1, 2, 3, 3, 4, 10]
    sauron_score_list = [1, 2, 2, 2, 3, 5, 10]

    gandalf = list(map(int, sys.stdin.readline().split()))
    sauron = list(map(int, sys.stdin.readline().split()))

    gandalf_score = 0
    sauron_score = 0

    for j in range(len(gandalf)):
        gandalf_score += gandalf[j] * gandalf_score_list[j]
    for k in range(len(sauron)):
        sauron_score += sauron[k] * sauron_score_list[k]

    print("Battle {i}:".format(i=i), end=" ")

    if gandalf_score > sauron_score:
        print("Good triumphs over Evil")
    elif gandalf_score < sauron_score:
        print("Evil eradicates all trace of Good")
    else:
        print("No victor on this battle field")


