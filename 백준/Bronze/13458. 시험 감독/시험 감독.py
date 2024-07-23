import sys
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
b,c=map(int,sys.stdin.readline().split())
total=n
for i in a:
    if i>=b:
        if (i-b)%c!=0:
            total+=((i-b)//c+1)
        else:
            total+=(i-b)//c
print(total)