import sys
def dfs(x,y):
    visited[x][y]=1
    if graph[x][y]=='-':
        if y+1<m and graph[x][y+1]=='-' and visited[x][y+1]==0:
            dfs(x,y+1)
        else:
            return
    if graph[x][y]=='|':
        if x+1<n and graph[x+1][y]=='|' and visited[x+1][y]==0:
            dfs(x+1,y)
        else:
            return  
n,m=map(int,sys.stdin.readline().split())
graph=[]
visited=[[0]*m for _ in range(n)]
cnt=0
for i in range(n):
    graph.append(sys.stdin.readline().rstrip())
for i in range(n):
    for j in range(m):
        if visited[i][j]==0:
            dfs(i,j)
            cnt+=1
print(cnt)        