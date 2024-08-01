import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
hx,hy=map(int,sys.stdin.readline().split())
ex,ey=map(int,sys.stdin.readline().split())
map=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,-1,1]
visited=[[[0,0] for _ in range(m)] for _ in range(n)]
ways=[]
def bfs(x,y):
    q=deque([(x,y,0)])
    visited[x][y][0]=1
    while q:
        x,y,magic=q.popleft()        
        if x==ex-1 and y==ey-1:
            return visited[x][y][magic]-1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                #빈칸인 경우
                if map[nx][ny]==0 and visited[nx][ny][magic]==0:
                    visited[nx][ny][magic]=visited[x][y][magic]+1
                    q.append((nx,ny,magic))
                #벽이고 마법 사용한적 없을때
                elif map[nx][ny]==1 and magic==0 and visited[nx][ny][1]==0:
                    visited[nx][ny][1]=visited[x][y][magic]+1
                    q.append((nx,ny,1))
    return -1
print(bfs(hx-1,hy-1))           
