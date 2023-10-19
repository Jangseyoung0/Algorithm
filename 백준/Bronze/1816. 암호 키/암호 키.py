import sys
n=int(sys.stdin.readline())
for _ in range(n):
    num=int(sys.stdin.readline())
    for i in range(2,1000001):
        if num%i==0:
            print("NO")
            break
        if i==1000000:
            print("YES")