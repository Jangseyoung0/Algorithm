import sys
from collections import deque
board=[list(map(int,sys.stdin.readline().split())) for _ in range(5)]
r,c=map(int,sys.stdin.readline().split())
dx=[-1,1,0,0]
dy=[0,0,1,-1]
visited=[[0]*5 for _ in range(5)]
def bfs(r,c):
    q=deque([(r,c)])
    visited[r][c]=0
    while q:
        x,y=q.popleft()
        if board[x][y]==1:
            return visited[x][y]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<5 and 0<=ny<5 and visited[nx][ny]==0 and board[nx][ny]!=-1:
                visited[nx][ny]=visited[x][y]+1
                q.append((nx,ny))

    return -1
print(bfs(r,c))