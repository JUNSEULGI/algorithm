N = int(input())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

def compareSize(n):
    x = arr[n][0]
    y = arr[n][1]
    rank = 1
    for c in arr:
        if x < c[0] and y < c[1]:
            rank += 1
    print(rank, end=' ')

for i in range(N):
    compareSize(i)
