import sys
n=int(sys.stdin.readline())
cnt=0
if n%5==0:
    cnt+=n//5
else:
    if n>5 and n%5%2==0:
        cnt+=n//5
        n%=5
        cnt+=n//2
        n%=2
    elif n>5 and n%5%2!=0:
        cnt+=(n//5-1)
        n-=cnt*5
        cnt+=n//2
        n%=2
    else:
        cnt+=n//2
        n%=2
if n==1:
    print(-1)
else:
    print(cnt)