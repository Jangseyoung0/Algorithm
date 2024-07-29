import sys
k=int(sys.stdin.readline())
bi=bin(k)
if bi.count('1')==1:
    print(k,0)
else:
    size=2**(len(bi)-2)
    for i in range(2,len(bi)):
        if bi[i]=='1':
            cnt=i-1
    print(size,cnt)