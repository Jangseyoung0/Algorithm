import sys
n,m=map(int,sys.stdin.readline().split())
arr=[]
for i in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))
minv=min(n,m)
l=0
for i in range(n):
    for j in range(m):
        for k in range(minv):
            if i+k<n and j+k<m and arr[i][j]==arr[i][j+k]==arr[i+k][j]==arr[i+k][j+k]:
                l=max(l,(k+1)**2)
print(l)