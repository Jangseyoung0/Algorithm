import sys
n,m=map(int,sys.stdin.readline().split())
row=[]
column=[]
bingo=[]
for i in range(n):
    bingo.append(list(map(int,sys.stdin.readline().split())))
for i in range(n):
    c=0
    for j in range(len(bingo[i])):
        for k in str(bingo[i][j]):
            if k=='9':
                c+=1
    row.append(c)
for i in range(m):
    c=0
    for j in range(n):
        for k in str(bingo[j][i]):
            if k=='9':
                c+=1
    column.append(c)
if max(row)>max(column):
    print(sum(row)-max(row))
else:
    print(sum(column)-max(column))