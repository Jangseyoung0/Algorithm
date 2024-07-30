import sys
from collections import deque
r,c=map(int,sys.stdin.readline().split())
graph=[list(sys.stdin.readline().rstrip()) for _ in range(r)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def bfs(x,y):
    q=deque([(x,y)])
    wo,sh=0,0
    if graph[x][y]=='v':
        wo=1
    if graph[x][y]=='o':
        sh=1  
    graph[x][y]='#'  
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<r and 0<=ny<c and graph[nx][ny]!='#':                
                if graph[nx][ny]=='v':
                    wo+=1
                if graph[nx][ny]=='o':
                    sh+=1
                graph[nx][ny]='#'
                q.append([nx,ny])
    return wo,sh
wolf=0
sheep=0
for i in range(r):
    for j in range(c):
        if graph[i][j]=='v' or graph[i][j]=='o':
            wo,sh=bfs(i,j)
            if wo>=sh:
                wolf+=wo
            else:
                sheep+=sh
print(sheep,wolf)