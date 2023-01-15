# isPrime 함수에서 걸러질 수 없는 예외값 미리 넣어둠
primeArr = [3, 5]

def isPrime(n):
    for i in range(3, n // 2 + 1):
        # 어차피 홀수이므로 3부터 쭉 나눠보고 나눠떨어지면 소수가 아니라 판단
        if n % i == 0:
            return False
    # 한번도 나눠떨어지지 않고 for문이 끝나면 소수
    primeArr.append(n)
    return True

def goldbach(n):
    # a가 작을수록 b - a가 크므로 a는 3부터 오름차순으로 확인
    a = 3
    while a <= n // 2:
        # a가 소수인지 확인, 소수가 아니면 패스
        if a in primeArr == False and isPrime(a) == False:
            a += 2
            continue
        b = n - a
        # a는 소수, b도 소수인지 확인
        if b in primeArr or isPrime(b):
            return "%d = %d + %d" % (n, a, b)
        a += 2
    return "Goldbach's conjecture is wrong."

numbers = map(int, input('4보다 큰 짝수를 입력하세요').split())
for i in numbers:
    if i == 0: break
    print(goldbach(i))