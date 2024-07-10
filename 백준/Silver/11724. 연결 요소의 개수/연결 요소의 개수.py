import sys
sys.setrecursionlimit(100000)
n,m=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
visited=[0]*(n+1)
def dfs(v):
    visited[v]=1
    for i in graph[v]:
        if visited[i]==0:
            dfs(i)
    return True
cnt=0
for i in range(1,n+1):
    if visited[i]==0:
        dfs(i)
        cnt+=1
print(cnt)