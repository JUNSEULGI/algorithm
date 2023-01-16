primeList = []

def isPrime(n):
    if n in primeList:
        return True
    mean = int(n ** (1/2))
    for i in range(2, mean + 1):
        if n % i == 0:
            return False
        if i == mean:
            primeList.append(n)
            return True

for i in range(2, 2 * 123456 + 1):
    isPrime(i)

def countPrimes(n):
    count = 0
    for i in range(n + 1, 2 * n + 1):
        if isPrime(i):
            count += 1
    return count

n = -1
while n != 0:     
    n = int(input())
    print(countPrimes(n))