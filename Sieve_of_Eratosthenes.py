def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

def prime_list_custom(n):
    prime_flag = [True] * (n+1)

    prime_num_list = []

    prime_flag[0] = False
    prime_flag[1] = False

    for i in range(2, n+1):
        if prime_flag[i]:
            for j in range(n):
                if i*j > n:
                    break
                prime_flag[i*j] = False
            prime_num_list.append(i)
    
    return prime_num_list
            
    



