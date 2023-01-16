numbers = list(map(int, input().split()))

def getGcd(a, b):
    if a >= b:
        [large, small] = [a, b]
    else:
        [large, small] = [b, a]
    if large % small == 0:
        return small
    gcd = 1
    for i in range(small // 2 , 1, -1):
        if (small % i == 0) and (large % i == 0):
            gcd = i
            break
    return gcd

gcd = getGcd(numbers[0], numbers[1])
print(gcd)
print(int(numbers[0] * numbers[1] / gcd))