import sys
sys.setrecursionlimit(1000000)
m,n=map(int,sys.stdin.readline().split())
graph=[]
for _ in range(m):
    graph.append(list(sys.stdin.readline().rstrip()))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
visited=[[0]*n for _ in range(m)]
def dfs(x,y):
    global ans
    if x==m-1:
        ans=1
        return True
    if 0<=x<m and 0<=y<n and graph[x][y]=='0' and visited[x][y]==0:
        visited[x][y]=1         
        for i in range(4):
            dfs(x+dx[i],y+dy[i])
ans=0  
flg=0
for i in range(n):
    dfs(0,i)
    if ans==1:
        flg=1
if flg==1:
    print("YES")
else:
    print("NO")