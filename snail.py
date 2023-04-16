N = int(input())
targetNumber = int(input())
targetLocation = []

# 좌표 모양의 배열 (각 요소는 y번째 줄을 나타내는 배열)
arr = [[0 for _ in range(N)] for _ in range (N)]

# 1은 위로, 2는 오른쪽으로, 3은 아래로, 4는 왼쪽으로
direction = 1 
# 전진해야 하는 줄 수
count = 2
# 현재 전진 횟수
now = 0
# 현재 y, x 좌표
y = x = 0

# 1부터 쭉 좌표를 계산하여 arr에서 해당 좌표 위치에 번호 저장
for i in range(N ** 2):
    if i == 0:
        median = (N + 1) // 2
        y = x = median - 1
    elif direction == 1:
        y -= 1
    elif direction == 2:
        x += 1
    elif direction == 3:
        y += 1
    elif direction == 4:
        x -= 1
    arr[y][x] = i + 1
    now += 1
    if i == targetNumber - 1:
        targetLocation = [y + 1, x + 1]
    if now == count:
        # 방향 바꿈
        if direction == 4:
            direction = 1
        else:
            direction += 1
        if direction % 2 != 0:
            count += 1
        now = 1

for y in range(N):
    for x in range(N):
        number = arr[y][x]
        if x == N - 1:
            print(number)
        else:
            print(number, end=' ')

print(targetLocation[0], targetLocation[1])