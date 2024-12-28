import sys

artist_set = set()
artist_double_set = set()

n = int(sys.stdin.readline())

for _ in range(n):
    artist = sys.stdin.readline().strip()
    if artist in artist_set:
        artist_double_set.add(artist)
    else:
        artist_set.add(artist)

print(len(artist_double_set))
