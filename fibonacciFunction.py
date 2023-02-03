countZero, countOne = 0, 0
czo = []

def fibonacci(n):
    if n == 0:
        global countZero
        countZero += 1
        return 0
    elif n == 1:
        global countOne
        countOne += 1
        return 1
    czo.append([countOne, countZero])
    return fibonacci(n - 1) + fibonacci(n - 2)


def countZeroAndOne(n):
    global countZero, countOne
    countZero, countOne = 0, 0

    fibonacci(n)
    print(countZero, countOne)

T = int(input())

for _ in range(T):
    n = int(input())
    countZeroAndOne(n)