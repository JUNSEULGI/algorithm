def isCompleted(n, arr, size, w):
    for i in range(n):
        if i == n - 1:
            if arr[i] + w / 2 >= size:
                return True
            else:
                return False
        if i == 0:
            if arr[i] > w / 2:
                return False
        if arr[i+1] - arr[i] > w:
            return False

while True:
    grass = input()
    if grass == '0 0 0.0':
        break
    array = grass.split()
    nx, ny, w = int(array[0]), int(array[1]), float(array[2])
    xi = sorted(list(map(float, input().split()))) # 가로에 평행하게 깎는 길들의 실수 좌표
    yi = sorted(list(map(float, input().split()))) # 세로에 평행하게 깎는 길들의 실수 좌표
    if isCompleted(nx, xi, 75, w) and isCompleted(ny, yi, 100, w):
        print('YES')
    else:
        print('NO')