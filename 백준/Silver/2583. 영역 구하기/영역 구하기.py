import sys
sys.setrecursionlimit(10**6)
m,n,k=map(int,sys.stdin.readline().split())
graph=[[0]*n for _ in range(m)]
for _ in range(k):
    x1,y1,x2,y2=map(int,sys.stdin.readline().split())
    for i in range(m-y2,m-y1):
        for j in range(x1,x2):
            graph[i][j]=1
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(x,y):
    graph[x][y]=1
    global cnt
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<m and 0<=ny<n and graph[nx][ny]==0:
            graph[nx][ny]=1
            cnt+=1
            dfs(nx,ny)
    return cnt
area=[]
for i in range(m):
    for j in range(n):
        if graph[i][j]==0:
            cnt=1
            area.append(dfs(i,j))
area.sort()
print(len(area))
print(*area)