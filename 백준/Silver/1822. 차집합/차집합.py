import sys
a,b=map(int,sys.stdin.readline().split())
ali=set(map(int,sys.stdin.readline().split()))
bli=set(map(int,sys.stdin.readline().split()))
c=ali-bli
c=sorted(list(c))
if len(c)>0:
    print(len(c))
    print(*c)
else:
    print(len(c))