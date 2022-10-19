import sys

while True:
    s = sys.stdin.readline().strip()
    if s == "-1":
        break
    else:
        n_list = list(map(int, s.split()))
        counter = 0
        for i in n_list:
            if i != 0 and (i*2) in n_list:
                counter += 1
        print(counter)

