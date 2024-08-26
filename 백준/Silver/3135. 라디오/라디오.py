import sys
a,b=map(int,sys.stdin.readline().split())
n=int(sys.stdin.readline())
k=[]
gap=[abs(a-b)]
for _ in range(n):
    k.append(int(sys.stdin.readline().rstrip()))
for i in k:
    gap.append(abs(i-b)+1)
print(min(gap))
