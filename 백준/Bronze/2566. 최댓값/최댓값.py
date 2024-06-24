import sys
li=[list(map(int,sys.stdin.readline().split()))for i in range(9)]
max=0
idx=0
idx2=0
for i in range(9):
    for j in range(9):
        if li[i][j]>max:
            max=li[i][j]
            idx=i
            idx2=j
print(max)
print(idx+1,idx2+1)