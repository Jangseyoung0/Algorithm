import sys
sys.setrecursionlimit(10000)
t=int(sys.stdin.readline())
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if graph[x][y]==1:
        graph[x][y]=0
        for i in range(4):
            dfs(x+dx[i],y+dy[i])
        return True
    return False

for _ in range(t):
    m,n,k=map(int,sys.stdin.readline().split())
    graph=[[0]*m for _ in range(n)]
    for i in range(k):
        y,x=map(int,sys.stdin.readline().split())
        graph[x][y]=1
    cnt=0
    for i in range(n):
        for j in range(m):
            if dfs(i,j)==1:
                cnt+=1
    print(cnt)