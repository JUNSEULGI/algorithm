def isPrime(n):
    if n==1:
        return False
    for i in range(2, int(n ** (1/2)) + 1):
        if n % i == 0:
            return False
    return True

def goldbach(n):
    for a in range(n // 2, 1, -1):
        if isPrime(a) == False:
            continue
        b = n - a
        if isPrime(b):
            return print(a, b)


for _ in range(int(input())):
    n=int(input())
    goldbach(n)