N, K = map(int, input().split())
A = list(map(int, input().split()))

count = 0

def swap(i):
    global count
    temp = A[i+1]
    A[i+1] = A[i]
    A[i] = temp
    count += 1
    if count == K:
        print(A[i], A[i+1])


def bubble(arr):
    global count
    n = 1
    while n < N:
        for i in range(len(arr) - n):
            if arr[i] > arr[i+1]:
                swap(i)
        n += 1

bubble(A)
if count < K:
    print(-1)