import sys
from collections import deque
a,k=map(int,sys.stdin.readline().split())
visited=[-1]*(k+1)
def bfs(a):
    queue=deque([a])
    visited[a]=0
    while queue:
        c=queue.popleft()
        if c==k:
            print(visited[c])
        n=c+1
        if n<=k and visited[n]==-1:
            visited[n]=visited[c]+1
            queue.append(n)
        m=c*2
        if m<=k and visited[m]==-1:
            visited[m]=visited[c]+1
            queue.append(m)

bfs(a)