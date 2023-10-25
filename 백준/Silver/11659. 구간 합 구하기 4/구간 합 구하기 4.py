import sys
n,m=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
list_sum=[0]
total=0
for i in range(n):
    total+=arr[i]
    list_sum.append(total)
for i in range(m):
    j,k=map(int,sys.stdin.readline().split())
    print(list_sum[k]-list_sum[j-1])