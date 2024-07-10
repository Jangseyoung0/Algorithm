import sys
sys.setrecursionlimit(10**9)
graph=[]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
for _ in range(5):
    graph.append(list(map(int,sys.stdin.readline().split())))
visited=[[0]*5 for _ in range(5)]
r,c=map(int,sys.stdin.readline().split())

def dfs(x,y,dep,cnt):
    visited[x][y]=1
    if graph[x][y]==1:
        cnt+=1
    if cnt>1:
        return 1
    if dep>2:
        visited[x][y]=0
        return 0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<5 and ny>=0 and ny<5:
            if visited[nx][ny]==0 and graph[nx][ny]!=-1:
                if dfs(nx,ny,dep+1,cnt)==1:
                    return 1
    visited[x][y]=0
    return 0
print(dfs(r,c,0,0))