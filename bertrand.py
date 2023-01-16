# def isPrime(n):
#     if n == 1:
#         return 1
#     count = 0
#     for i in range(n + 1, 2 * n):
#         half = i // 2
#         for j in range(2, half + 1):
#             # 2부터 쭉 i를 나눠보고 나눠떨어지면 소수가 아니라 판단하고 패스
#             if i % j == 0:
#                 break
#             # 한번도 나눠떨어지지 않고 절반의 수치까지 오면 소수이므로 카운트
#             if j == half:
#                 count += 1
#     return count

# n = -1
# while n != 0:     
#     n = int(input('숫자를 입력하세요'))
#     print(isPrime(n))


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