import sys
n=int(sys.stdin.readline())
fruits=list(map(int,sys.stdin.readline().split()))

def max_len(n,fruits):
    if n<=2:
        return n 
    maxl=0
    fcount=[0]*10
    s=0
    fkind=0    
    for e in range(n):
        if fcount[fruits[e]]==0:
            fkind+=1
        fcount[fruits[e]]+=1
        while fkind>2:           
            fcount[fruits[s]]-=1
            if fcount[fruits[s]]==0: 
                fkind-=1
            s+=1
        maxl=max(maxl,e-s+1)
    return maxl
print(max_len(n,fruits))