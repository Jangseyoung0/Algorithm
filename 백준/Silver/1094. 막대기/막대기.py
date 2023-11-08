import sys
n=int(sys.stdin.readline())
pol=64
sum=0
cnt=0
while n>=sum:
    if sum+pol<=n:
        sum+=pol
        cnt+=1 
    else:
        pol/=2   
    if n==sum:
        break
print(cnt)