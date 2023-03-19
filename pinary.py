# Fn(An, Bn) → Fn+1(An+Bn, An) → Fn+2(An+Bn+An, An+Bn)

def pinary(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return pinary(n-1) + pinary(n-2)

n = int(input())
print(pinary(n))