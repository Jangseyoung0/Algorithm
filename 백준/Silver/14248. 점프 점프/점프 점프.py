import sys
sys.setrecursionlimit(10**6)
n=int(sys.stdin.readline().rstrip())
rocks=list(map(int,sys.stdin.readline().rstrip().split()))
s=int(sys.stdin.readline())
cnt=1
v=[0]*n
def dfs(x):
    global cnt
    for nx in (x+rocks[x],x-rocks[x]):
        if 0<=nx<n and v[nx]==0:
            cnt+=1
            v[nx]=1
            dfs(nx)
dfs(s-1)
print(cnt)