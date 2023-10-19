import sys
T=int(sys.stdin.readline())
for _ in range(T):
    x,y=map(int,sys.stdin.readline().split())
    d=y-x
    m=(int)(d**0.5)
    cnt=m*2-1
    if d-m**2>0:
        cnt+=(d-m**2-1)//m+1
    print(cnt)       