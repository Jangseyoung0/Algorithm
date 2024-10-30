import sys
n=int(sys.stdin.readline())
a=[0]*10001
for _ in range(n):
    m=int(sys.stdin.readline())
    a[m]+=1

for i in range(10001):
    if a[i]!=0:
        for j in range(a[i]):
            print(i)