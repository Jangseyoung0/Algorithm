import sys
n=int(sys.stdin.readline())
map=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
count=[[] for _ in range(n)]
for i in range(n):
    c=0
    for j in range(5):
        for k in range(n):
            if map[i][j]==map[k][j] and i!=k :
                count[i].append(k)
for i in range(n):
    count[i]=len(list(set(count[i])))
print(count.index(max(count))+1)
      