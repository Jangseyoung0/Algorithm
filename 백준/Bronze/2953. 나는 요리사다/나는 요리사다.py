import sys
max=0
maxi=0
for i in range(5):
    sli=list(map(int,sys.stdin.readline().split()))
    if sum(sli)>max:
        maxi=i+1
        max=sum(sli)
        
print(maxi,max)