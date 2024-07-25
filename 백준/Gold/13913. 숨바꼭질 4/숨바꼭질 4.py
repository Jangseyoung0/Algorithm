import sys
from collections import deque
n,k=map(int,sys.stdin.readline().split())
visited=[-1]*(100001)
re=[-1]*(100001)
def bfs(x):
    q=deque([x])
    visited[x]=0
    while q:
        c=q.popleft()
        if c==k:
          return visited[c]
        for i in [c-1,c+1,c*2]:
            if 0<=i<=100000 and visited[i]==-1:
                q.append(i)
                visited[i]=visited[c]+1
                re[i]=c
def path(k):
    path=[]
    while k!=-1:
        path.append(k)
        k=re[k]
    path.reverse()
    return path

print(bfs(n))
print(*path(k),sep=' ')