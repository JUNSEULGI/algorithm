N, K = map(int, input().split())
A = list(map(int, input().split()))

def insertion(arr, N, K):
    count = 0
    for i in range(1, N):
        # 현재 정렬 완료된 것까지 위치
        location = i - 1
        newItem = arr[i]
        # 새로 비교할 수가 앞의 수보다 크면 제자리에 있는 거니까 패스
        if newItem > arr[location]:
            continue
        # 새로 비교하는 수가 제자리에 갈 때까지(앞의 수보다 커질 때까지), 더 큰 수들을 뒤로 보냄
        while location >= 0 and newItem < arr[location]:
            arr[location + 1] = arr[location]
            count += 1
            if count == K:
                print(arr[location + 1])
            location -= 1
        arr[location + 1] = newItem
        count += 1
        if count == K:
            print(arr[location + 1])
    if count < K:
        print(-1)

insertion(A, N, K)