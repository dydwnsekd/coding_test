import sys

artist_list = []
artist_double_list = []

n = int(sys.stdin.readline())

for i in range(n):
    artist = sys.stdin.readline().strip()
    if artist in artist_list:
        if artist in artist_double_list:
            pass
        else:
            artist_double_list.append(artist)
    else:
        artist_list.append(artist)

print(len(artist_double_list))
