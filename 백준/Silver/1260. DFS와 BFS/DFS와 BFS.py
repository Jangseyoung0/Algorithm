import sys
sys.setrecursionlimit(10**6)
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
result=[]
def dfs(r):
    visited[r]=1
    result.append(r)
    for i in graph[r]:
        if visited[i]==0:
            visited[i]=1
            dfs(i)
    return result
arr=[]
count=1
def bfs(r):
    global n
    visited=[0]*(n+1)
    q=deque([r])
    visited[r]=1
    while q:
        c=q.popleft()
        arr.append(c)
        for n in graph[c]:
            if visited[n]==0:
                visited[n]=1
                q.append(n)
    return arr
print(*dfs(r))
print(*bfs(r))