import sys
sys.setrecursionlimit(10**6)
from collections import deque
a,b=map(int,sys.stdin.readline().split())
n,m=map(int,sys.stdin.readline().split())
graph=[[]for _ in range(n+1)]
for _ in range(m):
    t,p=map(int,sys.stdin.readline().split())
    graph[t].append(p)
    graph[p].append(t)
visited=[-1]*(n+1)
def bfs(a,b):
    visited[a]=0
    q=deque([a])
    while q:
        nq=q.popleft()
        if nq==b:
            return visited[nq]         
        for x in graph[nq]:
            if visited[x]==-1:
                q.append(x)
                visited[x]=visited[nq]+1
    return -1
print(bfs(a,b))