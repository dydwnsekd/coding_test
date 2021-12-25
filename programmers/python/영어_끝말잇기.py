# https://programmers.co.kr/learn/courses/30/lessons/12981
def solution(n, words):
    answer = []
    duplicate_word = [words[0]]
    end_word = words[0][-1]

    for i in range(1, len(words)):
        if words[i] in duplicate_word or end_word != words[i][0]:
            return [i%n + 1, i//n + 1]
        else:
            duplicate_word.append(words[i])
            end_word = words[i][-1]

    return [0,0]