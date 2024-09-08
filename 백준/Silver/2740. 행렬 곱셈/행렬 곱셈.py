import sys
n,m=map(int,sys.stdin.readline().split())
a=[]
for i in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))
m,k=map(int,sys.stdin.readline().split())
b=[]
for i in range(m):
    b.append(list(map(int,sys.stdin.readline().split())))
re=[[] for _ in range(n)]
for i in range(n):
    for j in range(k):
        sum=0
        for h in range(m):
            sum+=a[i][h]*b[h][j]
        re[i].append(sum)
for i in range(n):
    print(*re[i])