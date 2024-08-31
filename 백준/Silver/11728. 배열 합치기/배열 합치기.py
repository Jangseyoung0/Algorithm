import sys
n,m=map(int,sys.stdin.readline().split())
li=[]
for _ in range(2):
    a=list(map(int,sys.stdin.readline().split()))
    for j in range(len(a)):
        li.append(a[j])
li.sort()
print(*li)