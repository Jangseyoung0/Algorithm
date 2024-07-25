import sys
from collections import deque
n,k=map(int,sys.stdin.readline().split())
visited=[-1]*(100001)
ways=[]
def bfs(n):
    visited[n]=0
    q=deque([n])
    while q:
        c=q.popleft()
        if c==k:
            ways.append(visited[c])     
        for i in [c-1,c+1,c*2]:
            if 0<=i<=100000:
                if visited[i]==-1 or visited[i]==visited[c]+1:
                    visited[i]=visited[c]+1 
                    q.append(i)  
bfs(n)
print(ways[0])
print(len(ways))
