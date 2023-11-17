import sys
n=int(sys.stdin.readline().strip())
arr=list(map(int,sys.stdin.readline().split()))
arr=set(arr)
arr=sorted(arr)
for i in arr:
    print(i,end=' ')