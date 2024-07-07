import sys
s=sys.stdin.readline().rstrip()
dict={}
alp='abcdefghijklmnopqrstuvwxyz'
for i in alp:
    dict[i]=0
for i in s:
    dict[i]+=1
print(' '.join(map(str,dict.values())))