import sys

keyboard_dict = {
    'a': 'q',
    'b': 'w',
    'c': 'e',
    'd': 'r',
    'e': 't',
    'f': 'y',
    'g': 'u',
    'h': 'i',
    'i': 'o',
    'j': 'p',
    'k': 'a',
    'l': 's',
    'm': 'd',
    'n': 'f',
    'o': 'g',
    'p': 'h',
    'q': 'j',
    'r': 'k',
    's': 'l',
    't': 'z',
    'u': 'x',
    'v': 'c',
    'w': 'v',
    'x': 'b',
    'y': 'n',
    'z': 'm',
    ' ': ' ',
}

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
change_s = ''

for c in s:
    change_s += keyboard_dict[c]

print(change_s)
