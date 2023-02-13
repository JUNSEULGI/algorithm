# Fn = Fn-1 + 2Fn-2
arr = [0 for _ in range(251)]
arr[0] = 1
arr[1] = 1
arr[2] = 3

def tile(n):
    if arr[n] != 0:
        return arr[n]
    count = tile(n-1) + 2 * tile(n-2)
    arr[n] = count
    return count

while True:
    try:
        n = int(input())
        print(tile(n))
    except:
        break