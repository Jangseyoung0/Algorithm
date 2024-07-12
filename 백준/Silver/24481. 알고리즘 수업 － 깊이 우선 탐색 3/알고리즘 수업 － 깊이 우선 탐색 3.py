import sys
sys.setrecursionlimit(10**6)
n,m,r=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(n+1):
    graph[i].sort()
visited=[-1]*(n+1)

def dfs(r,dep):
    visited[r]=dep
    for x in graph[r]:
        if visited[x]==-1:
            dfs(x,dep+1)
dfs(r,0)
print(*visited[1:],sep='\n')