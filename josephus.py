N, K = map(int, input().split())
numbers = []

for i in range(N):
    numbers.append(str(i+1))

result = []
endedIndex = 0

def josephus(arr, start, k):
    killed = (start + k - 1) % len(arr)
    result.append(arr.pop(killed))
    return killed

while len(numbers) > 0:
    endedIndex = josephus(numbers, endedIndex, K)

string = ', '.join(result)
print(f'<{string}>')