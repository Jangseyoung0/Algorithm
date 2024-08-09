import sys
n,m=map(int,sys.stdin.readline().split())
arr=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
k=int(sys.stdin.readline())
for _ in range(k):
    sum=0
    i,j,x,y=map(int,sys.stdin.readline().split())
    for a in range(i-1,x):
        for b in range(j-1,y):
            sum+=arr[a][b]
    print(sum)