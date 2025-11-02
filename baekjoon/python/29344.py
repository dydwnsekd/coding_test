import sys

s = sys.stdin.readline().strip()[:-1]
sentences = s[:-1].split('.')
result = ''

for sentence in sentences:
    result += ' '.join(sentence.split(' ')[::-1]) + '. '

print(result)

