# input settings
n = int(input())
target = int(input())

# init values
snail_matrix = [[0] * n for _ in range(n)]
value = n * n
row, column = 1, 1  # 행렬이므로 row = 가로축, column = 세로축
target_row, target_column = (n + 1) // 2, (n + 1) // 2

def move_like_a_snail(n, row, column):
    global value, target_row, target_column
    move = [[1, 0]] * (n-1) + [[0, 1]]* (n-1)+ [[-1, 0]]* (n-1)+ [[0, -1]]* (n-1)

    if n == 1:
        snail_matrix[column - 1][row - 1] = value
        return
    if n > 1:
        # 규칙: 하->우->상->좌 로 n-1씩 움직임
        for i in move:
            snail_matrix[column - 1][row - 1] = value
            if value == target:
                target_row = row
                target_column = column
            value -= 1
            column += i[0]
            row += i[1]
        move_like_a_snail(n - 2, row + 1, column + 1)


def print_arr(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end=" ")
        print()


# 재귀호출로 바꾸기
if n > 0:
    move_like_a_snail(n, row, column)

print_arr(snail_matrix)
print(target_column, target_row)