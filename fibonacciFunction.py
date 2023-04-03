czo = [[0, 0] for _ in range(41)]
czo[0] = [1,0]
czo[1] = [0,1]

def fibonacci(n):
    if czo[n][0] > 0 or czo[n][1] > 0:
        return czo[n]
    if czo[n-1][0] > 0 or czo[n-1][1] > 0:
        czo_1 = czo[n-1]
    else:
        czo_1 = fibonacci(n - 1)
    if czo[n-2][0] > 0 or czo[n-2][1] > 0:
        czo_2 = czo[n-2]
    else:
        czo_2 = fibonacci(n - 2)
    czo[n] = [czo_1[0] + czo_2[0], czo_1[1] + czo_2[1]]
    return czo[n]

def countZeroAndOne(n):
    fibonacci(n)
    print(czo[n][0], czo[n][1])

T = int(input())

for _ in range(T):
    n = int(input())
    countZeroAndOne(n)