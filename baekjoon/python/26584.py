import sys

cases = int(sys.stdin.readline())

min_hour = 60
min_day = min_hour * 24
min_year = min_day * 365

for _ in range(cases):
    game_name, playtime = sys.stdin.readline().strip().split(",")
    playtime = int(playtime)

    result_text = ""

    if playtime // min_year > 0:
        result_text += f"{playtime // min_year} year(s) "
        playtime = playtime % min_year

    if playtime // min_day > 0:
        result_text += f"{playtime // min_day} day(s) "
        playtime = playtime % min_day

    if playtime // min_hour > 0:
        result_text += f"{playtime // min_hour} hour(s) "
        playtime = playtime % min_hour

    if playtime > 0:
        result_text += f"{playtime} minute(s)"

    print(game_name + " - " + result_text)
