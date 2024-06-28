import sys
n=int(sys.stdin.readline())
f=2
for i in range(n):
    f=f*2-1
print(f**2)