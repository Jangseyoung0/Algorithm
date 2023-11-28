import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
cnt=0
for i in arr:
    if i==m:
        cnt+=1
print(cnt)