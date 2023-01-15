def printAscend(n):
  if n > 1:
    printAscend(n - 1)
  print(n)

def printEven(n):
  if n > 1:
    printEven(n - 1)
  if n % 2 == 0:
    print(n)

def printOdd(n):
  if n > 1:
    printOdd(n - 1)
  if n % 2 != 0:
    print(n)
  printDescEven(n)

def printDescEven(n):
  if n % 2 == 0:
    print(n)
  if n > 1:
    printDescEven(n - 1)
  printOdd(n)

# printAscend(100)
# printEven(100)
printOdd(100)