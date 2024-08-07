import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
x=int(sys.stdin.readline())
arr.sort()
s=0
e=n-1
cnt=0
while e>s:
    k=arr[s]+arr[e]
    if k==x:
        cnt+=1
        s+=1
        e-=1
    elif k<x:
        s+=1
    else:
        e-=1
print(cnt)