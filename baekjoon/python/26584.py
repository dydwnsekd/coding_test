import sys

cases = int(sys.stdin.readline())

time_dict = {"year(s)": 60 * 24 * 365, "day(s)": 60 * 24, "hour(s)": 60, "minute(s)": 1}

for _ in range(cases):
    game_name, playtime = sys.stdin.readline().strip().split(",")
    playtime = int(playtime)

    result_text = ""

    for k, v in time_dict.items():
        if playtime // v > 0:
            result_text += f"{playtime // v} {k} "
            playtime = playtime % v

    print(game_name + " - " + result_text)
