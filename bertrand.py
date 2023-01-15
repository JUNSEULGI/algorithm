def isPrime(n):
    if n == 1:
        return 1
    count = 0
    for i in range(n + 1, 2 * n):
        mean = int(i ** (1/2))
        for j in range(2, mean + 1):
            if i % j == 0:
                break
            if j == mean:
                count += 1
    return count

n = -1
while n != 0:     
    n = int(input())
    print(isPrime(n))