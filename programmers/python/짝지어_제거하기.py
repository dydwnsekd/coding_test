def solution(s):
    prev_len_s = 0
    while prev_len_s != len(s):
        prev_len_s = len(s)
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                if len(s) > i+2:
                    s = s[:i] + s[i+2:]
                    break
                else:
                    s = s[:i]
                    break
                    
    if s == "":
        return 1
    else:
        return 0