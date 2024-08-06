import sys
n,k=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))

maxs=sum(arr[:k])
curr=sum(arr[:k])
for i in range(k,len(arr)):
    curr+=arr[i]-arr[i-k]
    maxs=max(maxs,curr)
print(maxs)