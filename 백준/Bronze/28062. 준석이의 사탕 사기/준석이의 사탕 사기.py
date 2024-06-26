import sys
n=int(sys.stdin.readline())
ali=list(map(int,sys.stdin.readline().split()))
ali.sort()
odd=[]
total=sum(ali)
for i in ali:
    if i%2==1:
        odd.append(i)
if len(odd)%2==1:
    total-=odd[0]
print(total)