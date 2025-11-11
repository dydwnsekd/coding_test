import sys

movie_time = [3, 20, 120]

max_time = list(map(int, sys.stdin.readline().strip().split()))
mel_time = list(map(int, sys.stdin.readline().strip().split()))

max_view = 0
mel_view = 0

for i in range(3):
    max_view += max_time[i] * movie_time[i]
    mel_view += mel_time[i] * movie_time[i]

if max_view > mel_view:
    print("Max")
elif max_view < mel_view:
    print("Mel")
else:
    print("Draw")

