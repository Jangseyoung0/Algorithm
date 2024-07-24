import sys
c=0
while True:
    l,p,v=map(int,sys.stdin.readline().split())
    if l==0 and p==0 and v==0:
        break
    else:
        c+=1
        if v%p>l:
            vacation=(v//p)*l+l
        else:
            vacation=v%p+(v//p)*l
    print('Case ',c,': ',vacation,sep='')