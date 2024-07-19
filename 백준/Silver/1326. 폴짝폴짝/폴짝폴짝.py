import sys
from collections import deque
n=int(sys.stdin.readline())
graph=list(map(int,sys.stdin.readline().split()))
a,b=map(int,sys.stdin.readline().split())
visited=[-1]*n
def bfs(a):
    q=deque([a])
    visited[a]=0
    while q:
        x=q.popleft()
        jump=graph[x]
        for i in range(x,n,jump):
            if visited[i]==-1:
                q.append(i)
                visited[i]=visited[x]+1
                if i==b-1:
                    return visited[i]
        for i in range(x,-1,-jump):
            if visited[i]==-1:
                q.append(i)
                visited[i]=visited[x]+1
                if i==b-1:
                    return visited[i]
    return visited[b-1]
print(bfs(a-1))
