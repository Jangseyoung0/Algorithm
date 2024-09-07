import sys
n,m=map(int,sys.stdin.readline().split())
if n==0:
    print(0)
else:
    books=list(map(int,sys.stdin.readline().split()))
    box=0
    i=0
    while i<n:
        total=0
        while i<n and total+books[i]<=m:
            total+=books[i]
            i+=1
        box+=1
    print(box)