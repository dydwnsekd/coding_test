import sys

upper_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_list = "abcdefghijklmnopqrstuvwxyz"
num_list = "0123456789"

while True:
    upper_count = 0
    lower_count = 0
    num_count = 0
    blank_count = 0

    s = sys.stdin.readline().replace('\n', "")

    if s == "":
        break

    for i in s:
        if i in upper_list:
            upper_count += 1
        elif i in lower_list:
            lower_count += 1
        elif i in num_list:
            num_count += 1
        else:
            blank_count += 1

    """
        for i in s:
            if ord("A") <= ord(i) <= ord("Z"):
                upper_count += 1
            elif ord("a") <= ord(i) <= ord("z"):
                lower_count += 1
            elif ord("0") <= ord(i) <= ord("9"):
                num_count += 1
            else:
                blank_count += 1
    """

    print(lower_count, upper_count, num_count, blank_count)
