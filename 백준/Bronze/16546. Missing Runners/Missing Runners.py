import sys
n=int(sys.stdin.readline())
runner=list(map(int,sys.stdin.readline().split()))
arr=[i for i in range(1,n+1)]
print(*(set(arr)-set(runner)))