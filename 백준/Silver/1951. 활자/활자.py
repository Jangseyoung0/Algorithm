import sys
n=int(sys.stdin.readline())
nlen=len(str(n))
cnt=0
for i in range(1,nlen):
    cnt+=9*i*10**(i-1)
cnt+=nlen*(n-10**(nlen-1)+1)
print(cnt%1234567)