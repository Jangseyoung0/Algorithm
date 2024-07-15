import sys
n=int(sys.stdin.readline())
histo=list(map(int,sys.stdin.readline().split()))
total=n*2+sum(histo)*2+histo[0]+histo[-1]
for i in range(0,n-1):
    total+=abs(histo[i+1]-histo[i])
print(total)