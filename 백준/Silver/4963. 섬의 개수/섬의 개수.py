import sys
sys.setrecursionlimit(100000)
while True:
    w,h=map(int,sys.stdin.readline().split())
    if w==0 and h==0:
        break
    graph=[]
    for _ in range(h):
        graph.append(list(map(int,sys.stdin.readline().split())))
    dx=[-1,1,0,0,-1,1,-1,1]
    dy=[0,0,-1,1,1,-1,-1,1]
    cnt=0
    def dfs(x,y):    
        if x<0 or x>=h or y<0 or y>=w:
            return False
        if graph[x][y]==1:
            graph[x][y]=-1
            for i in range(8):
                dfs(x+dx[i],y+dy[i])            
            return True
        return False
    for i in range(h):
        for j in range(w):
            if dfs(i,j)==1:
                cnt+=1
    print(cnt)