numbers = input()
[m, n, p] = map(int, numbers.split())

def iteration(i):
  if i >= n:
    return
  print(i)
  iteration(i + p)

if m > n or p <= 0:
  print('IndexError')
else:
  iteration(m)