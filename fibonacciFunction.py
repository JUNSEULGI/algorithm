countZero, countOne = 0, 0
czo = [[0, 0] for _ in range(41)]

def fibonacci(n):
    global countZero, countOne
    if n == 0:
        countZero += 1
        return
    if n == 1:
        countOne += 1
        return
    if czo[n][0] > 0:
        countZero += czo[n][0]
        countOne += czo[n][1]
        return
    fibonacci(n - 2)
    fibonacci(n - 1)
    czo[n] = [countZero, countOne]
    return

# f(4)
#     f(2)
#         f(0) f(1)
#         저장
#     f(3)
#         f(1) f(2)
#         저장
#     저장

def countZeroAndOne(n):
    global countZero, countOne
    countZero, countOne = 0, 0
    fibonacci(n)
    print(countZero, countOne)

T = int(input())

for _ in range(T):
    n = int(input())
    countZeroAndOne(n)