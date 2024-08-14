import sys
n=int(sys.stdin.readline())
nlen=len(str(n))
cnt=0
for i in range(nlen-1):
    cnt+=9*10**i*(i+1)
cnt+=(n-10**(nlen-1)+1)*nlen
print(cnt)
    