N = int(input())
target = int(input())

# [y, x]
arr = [[[0] for _ in range(2)] for _ in range(N ** 2)]

# 1은 위로, 2는 오른쪽으로, 3은 아래로, 4는 왼
direction = 1 
# 전진해야 하는 줄 수
count = 2
# 현재 전진 횟수
now = 0

# 각 숫자의 좌표 저장
for i in range(N ** 2):
    if i == 0:
        arr[i] = [(N + 1) // 2, (N + 1) // 2]
        now += 1
        continue
    prevY = arr[i-1][0]
    prevX = arr[i-1][1]
    print(i, prevY, prevX, 'new direction', direction)
    if direction == 1:
        arr[i][0] = prevY - 1
        arr[i][1] = prevX
    elif direction == 2:
        arr[i][0] = prevY
        arr[i][1] = prevX + 1
    elif direction == 3:
        arr[i][0] = prevY + 1
        arr[i][1] = prevX
    elif direction == 4:
        arr[i][0] = prevY
        arr[i][1] = prevX - 1
    now += 1
    if now == count:
        # 방향 바꿈
        if direction == 4:
            direction = 1
        else:
            direction += 1
        if direction % 2 != 0:
            count += 1
        now = 1

print(arr)
snail = [0] * (N ** 2)
for i in range(N ** 2):
    y = arr[i][0]
    x = arr[i][1]
    index = (y - 1) * N + x - 1
    snail[index] = i + 1

for i in range(N ** 2):
    number = snail[i]
    if (i + 1) % N == 0:
        print(number)
    else:
        print(number, end=' ')

print(arr[target - 1])