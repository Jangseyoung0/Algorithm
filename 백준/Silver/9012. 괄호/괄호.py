import sys
n=int(sys.stdin.readline())
for _ in range(n):
    gh=sys.stdin.readline().rstrip()
    count=[]
    flag=0
    for i in gh:
        if i=='(':
            count.append(i)
        else:
            if len(count)>0:
                count.pop()
            else:
                flag=1
                break
    if flag==0 and len(count)==0:
        print("YES")
    else:
        print("NO")
