import sys
from collections import Counter
n,m=map(int,sys.stdin.readline().split())
dict={}
dnali=[]
for _ in range(n):
    dnali.append(sys.stdin.readline().rstrip())
result=''
sum=0
for i in range(m):
    cols=[dnali[j][i] for j in range(n)]
    mostc=Counter(cols).most_common()
    mostc.sort(key=lambda x : (-x[1],x[0]))
    result+=mostc[0][0]
for i in range(n):
    for j in range(m):
        if result[j]!=dnali[i][j]:
            sum+=1
print(result)
print(sum)