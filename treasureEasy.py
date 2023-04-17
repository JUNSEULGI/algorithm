N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# S가 가장 작으려면 배열 B에서 대응하는 숫자와 순서가 반대여야 함
# B의 숫자의 크기 순위를 구하고
# A의 숫자를 이 순위의 반대로 정렬한다

def sort(arr):
    for i in range(N-1, 0, -1):
        maxIndex = arr.index(max(arr[:i+1]))
        if arr[maxIndex] == arr[i]:
            continue
        arr[i], arr[maxIndex] = arr[maxIndex], arr[i]
    return arr
        
def minS(A, B, N):
    # A는 오름차순 정렬
    sortedA = sort(A)
    # B는 내림차순 정렬
    sortedB = sort(B)
    sortedB.reverse()
    S = 0
    for i in range(N):
        S += sortedA[i] * sortedB[i]
    return S

print(minS(A, B, N))