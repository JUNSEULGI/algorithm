n=int(input())

arr=[[0]*(n+1)]*(n+1)
print(arr)

def printarr(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end=" ")
        print()


y=1
x=1
num=n*n
step = [[1,0],[0,1],[-1,0],[0,-1]]
stepindex=0

for _ in range(n*n):
    print(y,x)
    arr[y][x]=num
    printarr(arr)
    num-=1
    nexty=y+step[stepindex][0]
    nextx=x+step[stepindex][1]
    if nexty<1 or nexty>n or nextx<1 or nextx>n or arr[nexty][nextx] !=0:
        stepindex = (stepindex+1)%4
        nexty=y+step[stepindex][0]
        nextx=x+step[stepindex][1]
    y=nexty
    x=nextx
    
printarr(arr)