import sys
n=int(sys.stdin.readline())
graph=[]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
visited=[[0]*n for _ in range(n)]
def dfs(x,y):
    visited[x][y]=1
    if x+graph[x][y]<n and visited[x+graph[x][y]][y]==0:
        dfs(x+graph[x][y],y)
    if y+graph[x][y]<n and visited[x][y+graph[x][y]]==0:
        dfs(x,y+graph[x][y])
dfs(0,0)
if visited[n-1][n-1]==1:
    print("HaruHaru")
else:
    print("Hing")
