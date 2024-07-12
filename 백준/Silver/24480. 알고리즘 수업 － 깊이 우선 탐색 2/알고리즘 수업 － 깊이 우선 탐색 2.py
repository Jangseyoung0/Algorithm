import sys
sys.setrecursionlimit(10**6)
n,m,r=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(n+1):
    graph[i].sort(reverse=True)
visited=[0]*(n+1)
cnt=0
def dfs(r):
    global cnt
    cnt+=1
    visited[r]=cnt
    for x in graph[r]:
        if visited[x]==0:
            dfs(x)
dfs(r)
print(*visited[1:],sep='\n')