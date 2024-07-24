import sys
l,c=map(int,sys.stdin.readline().split())
alp=list(sys.stdin.readline().rstrip().split(' '))
alp.sort()
mo=['a','e','i','o','u']
p=[]
def mocheck(p):
    m,j=0,0
    for i in p:
        if i in mo:
            m+=1
        else:
            j+=1
    if m>=1 and j>=2:
        return True
    else:
        return False
def dfs(x):
    if len(p)==l:
        if mocheck(p):
            print(*p,sep='')
        return
    for i in range(x,c):
        p.append(alp[i])
        dfs(i+1)
        p.pop()
dfs(0)