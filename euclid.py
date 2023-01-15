numbers = input()
[a, b] = numbers.split()

def calcGCD(a, b):
  if a % b == 0:
    print(b)
    return
  calcGCD(b, a % b)

calcGCD(int(a), int(b))