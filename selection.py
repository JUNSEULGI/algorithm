N, K = map(int, input().split())
A = list(map(int, input().split()))

def findMax(arr):
    largest = 0
    index = -1
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            index = i
    return (largest, index)

def selectionSort(arr, N, K):
    count = 0
    # 배열의 길이만큼 반복할 거임
    for i in range(N):
        # 비교할 배열의 길이는 하나씩 줄어나갈 거임
        if i == 0:
            currArr = arr
        else:
            currArr = arr[0:-i]
        # 비교할 배열 안에서 가장 큰 수와 위치를 구함
        largest, index = findMax(currArr)
        # 지금 마지막 위치에 가장 큰 수가 있는 게 아니면 스왑
        if currArr[-1] != largest:
            arr[index] = currArr[-1]
            arr[len(currArr)-1] = largest
            count += 1
            if count == K:
                print(currArr[-1], largest)
    if count < K:
        print(-1)

selectionSort(A, N, K)
