import sys
from collections import deque
dx=[0,0,1,-1,0,0]
dy=[0,0,0,0,-1,1]
dz=[-1,1,0,0,0,0]
def bfs(z,x,y):     
    q=deque([(z,x,y)])
    visited[z][x][y]=0
    while q:
        z,x,y=q.popleft()
        if floor[z][x][y]=='E':
            return visited[z][x][y]
        for i in range(6):
            nz=z+dz[i]
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nz<l and 0<=nx<r and 0<=ny<c:
                if (floor[nz][nx][ny]=='.' or floor[nz][nx][ny]=='E') and visited[nz][nx][ny]==-1:
                    visited[nz][nx][ny]=visited[z][x][y]+1
                    q.append((nz,nx,ny))
    return False

while True:
    l,r,c=map(int,sys.stdin.readline().split())
    if l==0 and r==0 and c==0:
        break
    floor=[]
    for i in range(l):
        floor.append([list(sys.stdin.readline().rstrip()) for _ in range(r)])
        space=sys.stdin.readline().rstrip()
    visited=[[[-1]*c for _ in range(r)] for _ in range(l)]
    
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if floor[i][j][k]=='S':
                    a=bfs(i,j,k)
                    if not a:
                        print("Trapped!")
                    else:
                        print("Escaped in", a,"minute(s).")
