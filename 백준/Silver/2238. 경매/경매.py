import sys
u,n=map(int,sys.stdin.readline().split())
pli=[[] for _ in range(u+1)]
for i in range(n):
    name,price=sys.stdin.readline().strip().split()
    pli[int(price)].append(name)
t=0
for i in range(1,u+1):
    if len(pli[i])==1:
        print(pli[i][0],i)
        t=1     
        break
if t==0:
    minp=n+1
    mini=-1
    for i in range(1,u+1):  
        if 0<len(pli[i])<minp:
            minp=len(pli[i])
            mini=i
    if mini!=-1:        
        print(pli[mini][0],mini)