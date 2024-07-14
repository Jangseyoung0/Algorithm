import sys
sys.setrecursionlimit(10**6)
n,m=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n)]
for i in range(n):
    graph[i]=list(map(int,sys.stdin.readline().split()))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
res=[]
def dfs(x,y):
    graph[x][y]=0 
    global c
    c+=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
            dfs(nx,ny)
    return c

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            c=0
            res.append(dfs(i,j))
if len(res)==0:
    print(len(res),0,sep='\n')
else:
    print(len(res),max(res),sep='\n') 