import sys
from collections import deque
n,m,r=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(n):
    graph[i].sort()
visited=[0]*(n+1)
vcnt=1
dep=[-1]*(n+1)
def bfs(r):
    global vcnt
    visited[r]=1
    dep[r]=0
    q=deque([r])
    while q:
        cnode=q.popleft()
        for nnode in graph[cnode]:
            if visited[nnode]==0:
                vcnt+=1
                visited[nnode]=vcnt
                dep[nnode]=dep[cnode]+1
                q.append(nnode)
bfs(r)
total=0
for i in range(1,n+1):
    total+=visited[i]*dep[i]
print(total)