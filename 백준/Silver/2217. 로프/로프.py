import sys
n=int(sys.stdin.readline())
k=[]
for i in range(n):
    k.append(int(sys.stdin.readline().rstrip()))
k.sort()
w=[]
for i in k:
    w.append(i*n)
    n-=1
print(max(w))