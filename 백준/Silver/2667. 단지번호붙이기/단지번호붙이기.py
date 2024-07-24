import sys
n=int(sys.stdin.readline())
graph=[list(sys.stdin.readline().rstrip()) for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(x,y):
    graph[x][y]=0
    global cnt
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny]=='1':
            cnt+=1
            graph[nx][ny]='0'
            dfs(nx,ny)
    return cnt
map=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]=='1':
            cnt=1
            map.append(dfs(i,j))
map.sort()
print(len(map),*map,sep='\n')