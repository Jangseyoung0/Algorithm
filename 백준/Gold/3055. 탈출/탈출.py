import sys
from collections import deque
water=deque()
r,c=map(int,sys.stdin.readline().split())
map=[list(sys.stdin.readline().rstrip()) for _ in range(r)]
for i in range(r):
    for j in range(c):
        if map[i][j]=='*':
            water.append((i,j))
        if map[i][j]=='S':
            X=i
            Y=j
dx=[-1,1,0,0]
dy=[0,0,-1,1]
visited=[[0]*c for _ in range(r)]
def bfs(x,y):
    q=deque([(x,y)])
    visited[x][y]=1
    m=0
    while water or q:
        #물 지도 확장
        for _ in range(len(water)):
            wx,wy=water.popleft()
            for j in range(4):
                nx=wx+dx[j]
                ny=wy+dy[j]
                if 0<=nx<r and 0<=ny<c:
                    if map[nx][ny]=='.':
                        map[nx][ny]='*'
                        water.append((nx,ny))
        #고슴도치 이동
        for _ in range(len(q)):
            x,y=q.popleft()      
            if map[x][y]=='D':
                return visited[x][y]-1
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<r and 0<=ny<c:
                    if (map[nx][ny]=='.' or map[nx][ny]=='D') and visited[nx][ny]==0:
                        visited[nx][ny]=visited[x][y]+1
                        q.append((nx,ny)) 
    return "KAKTUS"
print(bfs(X,Y))