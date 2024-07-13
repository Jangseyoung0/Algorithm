import sys
sys.setrecursionlimit(10**6)
n,k=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    p,c=map(int,sys.stdin.readline().split())
    graph[p].append(c)
    graph[c].append(p)
apple=list(map(int,sys.stdin.readline().split()))
visited=[0]*(n+1)
cnt=0
def dfs(r,c):
    global cnt
    visited[r]=1
    if c>=0 and apple[r]==1:
        cnt+=1
    for x in graph[r]:
        if visited[x]==0:
            dfs(x,c-1)
dfs(0,k)
print(cnt)