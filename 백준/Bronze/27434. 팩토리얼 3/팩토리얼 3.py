import sys
n=int(sys.stdin.readline())
r=1
if n==0:
    print("1")
else:
    for i in range(1,n+1):
        r*=i
    print(r)