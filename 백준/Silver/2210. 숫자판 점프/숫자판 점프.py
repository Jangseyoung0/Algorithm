import sys
sys.setrecursionlimit(10**6)
board=[list(sys.stdin.readline().rstrip().split(' ')) for _ in range(5)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
nums=[]
def dfs(x,y,num):
    if len(num)==6:
        if num not in nums:
            nums.append(num)
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<5 and 0<=ny<5:
            dfs(nx,ny,num+board[nx][ny])
for i in range(5):
    for j in range(5):
        dfs(i,j,board[i][j])
print(len(nums))
    