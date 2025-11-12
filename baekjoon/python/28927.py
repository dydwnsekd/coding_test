"""
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
"""

import sys

movie_durations = [3, 20, 120]

max_scores = list(map(int, sys.stdin.readline().strip().split()))
mel_scores = list(map(int, sys.stdin.readline().strip().split()))

max_total = sum(a * b for a, b in zip(max_scores, movie_durations))
mel_total = sum(a * b for a, b in zip(mel_scores, movie_durations))

if max_total > mel_total:
    print("Max")
elif max_total < mel_total:
    print("Mel")
else:
    print("Draw")
