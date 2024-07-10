import sys
sys.setrecursionlimit(1000000)
t=int(sys.stdin.readline())

for _ in range(t):
    h,w=map(int,sys.stdin.readline().split())
    graph=[]
    for _ in range(h):
        graph.append(list(sys.stdin.readline().rstrip()))
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    visited=[[0]*w for _ in range(h)]
    def dfs(x,y):
        if x<0 or x>=h or y<0 or y>=w:
            return False
        if graph[x][y]=='#':
            graph[x][y]='.'
            for i in range(4):
                dfs(x+dx[i],y+dy[i])
            return True
        return False
    cnt=0
    for i in range(h):
        for j in range(w):
            if dfs(i,j)==1:
                cnt+=1
    print(cnt)