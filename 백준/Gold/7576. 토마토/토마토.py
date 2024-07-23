import sys
from collections import deque
m,n=map(int,sys.stdin.readline().split())
graph=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
f=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            f=1
if f==0:
    print(0)
    exit()
dx=[-1,1,0,0]
dy=[0,0,-1,1]
visited=[[-1]*m for _ in range(n)]
q=deque()
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            visited[i][j]=0
            q.append([i,j]) 
queue=deque()

while q:
    while q:
        queue.append(q.popleft())
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==-1:
                if graph[nx][ny]==0:
                    visited[nx][ny]=visited[x][y]+1
                    q.append((nx,ny))
max=0
for i in range(n):
    for j in range(m):
        if visited[i][j]==-1 and graph[i][j]==0:
            max=-1
            break
        if visited[i][j]>max:
            max=visited[i][j]
    if max==-1:
        break
print(max)