import sys
sys.setrecursionlimit(10**6)
n,m,k=map(int,sys.stdin.readline().split())
graph=[[0]*m for _ in range(n)]
for _ in range(k):
    r,c=map(int,sys.stdin.readline().split())
    graph[r-1][c-1]=1
dx=[-1,1,0,0]
dy=[0,0,-1,1]
visited=[[0]*m for _ in range(n)]

def dfs(x,y):
    global cnt
    visited[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
            if graph[nx][ny]==1:
                visited[nx][ny]=1
                cnt+=1
                dfs(nx,ny)
    return cnt
result=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]==1 and visited[i][j]==0:
            cnt=1
            result.append(dfs(i,j))
print(max(result))