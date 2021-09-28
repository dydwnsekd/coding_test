# https://programmers.co.kr/learn/courses/30/lessons/81301
def solution(s):
    string_to_num = {
                        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
                        "six": "6", "seven": "7", "eight": "8", "nine": "9"
                    }
    
    for k in string_to_num.keys():
        if k in s:
            s = s.replace(k, string_to_num[k])
            
    return int(s)