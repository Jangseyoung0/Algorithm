import sys
n,s,r=map(int,sys.stdin.readline().split())
damaged=list(map(int,sys.stdin.readline().split()))
morekayak=list(map(int,sys.stdin.readline().split()))
a=0
for i in range(s):
    if damaged[i] in morekayak:
        a+=1
        morekayak[morekayak.index(damaged[i])]=-1
        damaged[i]=-1
for i in range(s):
    if damaged[i]!=-1:
        if damaged[i]-1 in morekayak:
            a+=1
            morekayak[morekayak.index(damaged[i]-1)]=-1
        elif damaged[i]+1 in morekayak:
            a+=1
            morekayak[morekayak.index(damaged[i]+1)]=-1
print(s-a)
