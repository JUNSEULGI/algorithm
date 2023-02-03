# 일반함수 ver
# def fibonacci(n):
#   arr = [0, 1]
  
#   while len(arr) < n + 1:
#     new = arr[-1] + arr[-2]
#     arr.append(new)

#   print(arr[-1])


# 재귀함수 ver
# def fibonacci(n):
#   if n == 0:
#     return
#   if n == 1:
#     return 1
#   return fibonacci(n-1) + fibonacci(n-2)

# n = int(input())
# print(fibonacci(n))


# 2748
arr = [0 for _ in range(91)]
arr[1] = 1

def f(n):
  if n == 0:
    return 0
  if arr[n] > 0 :
    return arr[n]
  fibonacci = f(n-1) + f(n-2)
  arr[n] = fibonacci
  return fibonacci

n = int(input())
print(f(n))

# print(arr)
