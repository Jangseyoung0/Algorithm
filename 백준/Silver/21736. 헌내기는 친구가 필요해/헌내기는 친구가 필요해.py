import sys
sys.setrecursionlimit(1000000)
n,m=map(int,sys.stdin.readline().split())
graph=[]
for _ in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))
visited=[[0]*(m) for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
ans=0
def dfs(x,y):
    visited[x][y]=1
    if graph[x][y]=='P':
        global ans
        ans+=1  
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny]!='X' and visited[nx][ny]==0:
            dfs(nx,ny)
    return True
for i in range(n):
    for j in range(m):
        if graph[i][j]=='I':
            di=i
            dj=j
dfs(di,dj)
if ans==0:
    print("TT")
else:
    print(ans)