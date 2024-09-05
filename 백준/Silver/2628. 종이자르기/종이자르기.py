import sys
n,m=map(int,sys.stdin.readline().split())
t=int(sys.stdin.readline())
x=[0,n]
y=[0,m]
for _ in range(t):
    a,b=map(int,sys.stdin.readline().split())
    if a==0:
        y.append(b)
    else:
        x.append(b)
x.sort()
y.sort()
max=0
for i in range(len(x)-1):
    for j in range(len(y)-1):
        if (x[i+1]-x[i])*(y[j+1]-y[j])>max:
            max=(x[i+1]-x[i])*(y[j+1]-y[j])
print(max)