N, K = map(int, input().split())
A = list(map(int, input().split()))

counter = 0

def countUp(small, big):
    global counter, K
    counter += 1
    if counter == K:
        print(small, big)



def quick(arr, p, r):
    # if len(arr) <= 1:
    #     return
    if p < r:
        # q는 partition 한 결과로 알 수 있는 기준 위치
        q = partition(arr, p, r)
        # 왼쪽 배열 정렬
        quick(arr, p, q-1)
        quick(arr, q+1, r)


# arr는 정렬할 배열
# p는 ...?   
# r은 기준 원소의 위치 = 마지막 원소??
def partition(arr, p, r):
    # x는 기준 원소
    x = arr[r]
    # i는 기준 원소보다 작은 원소들의 마지막 지점 위치 <= p가 비교할 범위의 시작 위치이므로
    i = p - 1
    # j는 비교할 원소(탐색할 위치)
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            countUp(arr[i], arr[j])
    if i + 1 != r:
        arr[i+1], arr[r] = arr[r], arr[i+1]
        countUp(arr[i+1], arr[r])
    # 이때 i는 기준 원소보다 작은 원소의 마지막 위치
    return i + 1

print(N, K, A)
quick(A, 0, N-1)
print(A)
if counter < K:
    print(-1)