import sys
sys.setrecursionlimit(1000000)
n=int(sys.stdin.readline())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,sys.stdin.readline().split())     
    graph[a].append(b)
    graph[b].append(a)
visited=[0]*(n+1)
parentnode=[0]*(n+1)
def dfs(n):
    visited[n]=1
    for node in graph[n]:
        if visited[node]==0:
            parentnode[node]=n
            dfs(node)
dfs(1)
for i in range(2,n+1):
    print(parentnode[i])


