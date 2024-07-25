import sys
from collections import deque
r,c,n=map(int,sys.stdin.readline().split())
map=[list(sys.stdin.readline().rstrip()) for _ in range(r)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
q=deque()
for i in range(r):
    for j in range(c):
        if map[i][j]=='O':
            q.append([i,j])
t=1
while t<n:
    for i in range(r):
        for j in range(c):
            map[i][j]='O'
    t+=1
    if t==n:
        break
    while q:
        x,y=q.pop()
        map[x][y]='.'
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<r and 0<=ny<c:
                map[nx][ny]='.'
    for i in range(r):
        for j in range(c):
            if map[i][j]=='O':
                q.append([i,j])
    t+=1
for i in range(r):
    print(*map[i],sep='')