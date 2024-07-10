import sys
n=int(sys.stdin.readline())
a,b=map(int,sys.stdin.readline().split())
m=int(sys.stdin.readline())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    x,y=map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
visited=[0]*(n+1)
result=[]
def dfs(v,cnt): 
    cnt+=1
    visited[v]=1
    if v==b:
        result.append(cnt)
        return
    for i in graph[v]:
        if visited[i]==0:
            dfs(i,cnt)

dfs(a,0)
if len(result)==0:
    print(-1)
else:
    print(result[0]-1)