import sys

mirror_dict = {"b": "d", "d": "b", "p": "q", "q": "p", "i": "i", "o": "o", "v": "v", "w": "w", "x": "x"}

while True:
    str = sys.stdin.readline().strip()
    flag = True
    if str == "#":
        break
    else:
        str = str[::-1]
        mirror_str = ""
        for i in str:
            if i in mirror_dict.keys():
                mirror_str += mirror_dict[i]
            else:
                print("INVALID")
                flag = False
                break
        if flag:
            print(mirror_str)

