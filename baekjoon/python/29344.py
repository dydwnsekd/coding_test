import sys

s = sys.stdin.readline().strip()[:-1]
sentences = s.split('.')
result_list = []

for sentence in sentences:
    reversed_sentence = ' '.join(sentence.split()[::-1])
    result_list.append(reversed_sentence)

print('. '.join(result_list) + '.')

