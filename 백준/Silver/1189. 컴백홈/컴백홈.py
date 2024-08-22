import sys
sys.setrecursionlimit(10**6)
r,c,k=map(int,sys.stdin.readline().split())
graph=[]
for i in range(r):
    graph.append(list(sys.stdin.readline().rstrip()))
visited=[[0]*c for _ in range(r)]
dx=[0,0,-1,1]
dy=[-1,1,0,0]
cnt=0
def dfs(x,y,d):
    global cnt
    visited[x][y]==1
    if x==0 and y==c-1 and d==k:
        cnt+=1
    graph[x][y]='T'
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<r and 0<=ny<c and graph[nx][ny]=='.':
            graph[nx][ny]='T'
            dfs(nx,ny,d+1)
            graph[nx][ny]='.'
dfs(r-1,0,1)
print(cnt)