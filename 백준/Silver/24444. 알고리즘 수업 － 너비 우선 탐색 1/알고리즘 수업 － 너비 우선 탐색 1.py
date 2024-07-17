import sys
from collections import deque
n,m,r=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(n+1):
    graph[i].sort()
visited=[0]*(n+1)
cnt=1
def bfs(r):
    global cnt
    visited[r]=cnt
    q=deque()
    q.append(r)
    while q:
        cnode=q.popleft()
        for nnode in graph[cnode]:
            if visited[nnode]==0:
                cnt+=1
                visited[nnode]=cnt
                q.append(nnode)
bfs(r)
print(*visited[1:],sep='\n')
