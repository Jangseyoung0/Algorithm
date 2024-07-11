import sys
sys.setrecursionlimit(1000000)
n,m,r=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
visited=[0]*(n+1)
cnt=1
for i in range(n+1):
    graph[i].sort()
node=[]
def dfs(r):
    global cnt
    visited[r]=cnt
    cnt+=1  
    for x in graph[r]:
        if visited[x]==0:
            dfs(x)
dfs(r)
print(*visited[1:],sep='\n')