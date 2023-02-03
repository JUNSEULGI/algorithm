n = int(input())

def hanoiNumber(n):
    if n == 2:
        return 3
    return  2 * hanoiNumber(n - 1) + 1

print(hanoiNumber(n))

def hanoiProcess(n, start, mid, end):
    if n == 1:
        print(start, end)
        return
    if n > 1:
        hanoiProcess(n - 1, start, end, mid)
        print(start, end)
        hanoiProcess(n - 1, mid, start, end)

if n <= 20:
    hanoiProcess(n, 1, 2, 3)