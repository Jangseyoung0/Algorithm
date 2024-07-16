import sys
import copy
sys.setrecursionlimit(10**6)
n=int(sys.stdin.readline())
graph=[[] for _ in range(n)]
for i in range(n):
    graph[i]=list(sys.stdin.readline().rstrip())
visited=[[0]*n for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
cnt=0
rcnt=0
def dfs(x,y,k):
    visited[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny]==k and visited[nx][ny]==0:
            dfs(nx,ny,k)            
    return True
def dfs_rgb(x,y,k):
    visited[x][y]=0
    if k=='G' or k=='R':
        k=['G','R']
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] in k and visited[nx][ny]==1:
            dfs_rgb(nx,ny,k)
    return True
for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            if dfs(i,j,graph[i][j])==1:
                cnt+=1

for i in range(n):
    for j in range(n):
        if visited[i][j]==1:
            if dfs_rgb(i,j,graph[i][j])==1:
                rcnt+=1

print(cnt,rcnt)