import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

counter = 0


# p는 arr에서 정렬할 구간의 시작 인덱스, r은 마지막 인덱스
def mergeSort(arr, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    mergeSort(arr, start, mid)
    mergeSort(arr, mid + 1, end)
    merge(arr, start, mid, end)

def merge(arr, start, mid, end):
    global counter, K
    i = start  # 왼쪽 배열의 시작점
    j = mid + 1  # 오른쪽 배열의 시작점
    temp = [0]*(end+1 - start)  # 정렬된 숫자들을 임시로 담을 배열
    t = 0  # 비교한 숫자를 temp에 담을 위치
    while i <= mid and j <= end:  # 두 배열 중 어느 한 쪽을 끝까지 탐색 마칠 때까지
        if arr[i] <= arr[j]:
            temp[t] = arr[i]
            t += 1
            i += 1
        else:
            temp[t] = arr[j]
            t += 1
            j += 1
    while i <= mid: # 오른쪽 배열의 j가 먼저 끝난 경우
        temp[t] = arr[i]
        t += 1
        i += 1
    while j <= end: # 왼쪽 배열의 i가 먼저 끝난 경우
        temp[t] = arr[j]
        t += 1
        j += 1
    i = start
    t = 0
    while (i <= end):
        arr[i] = temp[t]
        counter += 1
        if counter == K:
            print(temp[t])
            exit()
        i += 1
        t += 1

mergeSort(A, 0, N-1)
print(-1)