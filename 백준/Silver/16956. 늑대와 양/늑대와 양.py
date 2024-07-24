import sys
from collections import deque
r,c=map(int,sys.stdin.readline().split())
graph=[list(sys.stdin.readline().rstrip()) for _ in range(r)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
visited=[[0]*c for _ in range(r)]
f=0
for i in range(r):
    for j in range(c):
        if graph[i][j]=='W':
            for k in range(4):
                nx=i+dx[k]
                ny=j+dy[k]
                if 0<=nx<r and 0<=ny<c and graph[nx][ny]=='S':
                    f=1
                    break
        elif graph[i][j]=='S':
            continue
        elif graph[i][j]=='.':
            graph[i][j]='D'
if f==1:
    print(0)
else:
    print(1)
    for i in range(r):
        print(*graph[i],sep='')