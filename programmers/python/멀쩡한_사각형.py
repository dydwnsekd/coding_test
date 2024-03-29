def getGCD(num1, num2):
    r = -1
    if num1 < num2: num1, num2 = num2, num1

    while (r!=0):
        r = num1 % num2
        num1, num2 = num2, r

    return(num1)

def solution(w,h):
    gcd = getGCD(w,h)
    
    return (w*h - (w+h-gcd))