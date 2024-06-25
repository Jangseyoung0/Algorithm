import sys
l,p=map(int,sys.stdin.readline().split())
ar=list(map(int,sys.stdin.readline().split()))
for i in range(len(ar)):
    ar[i]=ar[i]-(l*p)
print(*ar)