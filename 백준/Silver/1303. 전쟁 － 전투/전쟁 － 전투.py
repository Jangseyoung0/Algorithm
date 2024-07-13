import sys
sys.setrecursionlimit(10**9)
n,m=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(m)]
for i in range(m):
    graph[i]=list(sys.stdin.readline().rstrip())
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(x,y,c):
    global cnt
    cnt+=1
    graph[x][y]='V'
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<m and 0<=ny<n and graph[nx][ny]==c:            
            dfs(nx,ny,c)
    return cnt
wcnt=0
bcnt=0
for i in range(m):
    for j in range(n):
        cnt=0
        if graph[i][j]=='W':                 
            wcnt+=dfs(i,j,'W')**2
        if graph[i][j]=='B':          
            bcnt+=dfs(i,j,'B')**2
print(wcnt,bcnt)