import sys
from collections import deque
n,m,r=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
visited=[-1]*(n+1)
def bfs(r):
    q=deque([r])   
    visited[r]=0
    while q:
        cnode=q.popleft()
        for nnode in graph[cnode]:
            if visited[nnode]==-1:
                visited[nnode]=visited[cnode]+1
                q.append(nnode)
bfs(r)
print(*visited[1:],sep='\n')   