import sys
n=int(sys.stdin.readline())
friends=list(sys.stdin.readline())
h=sys.stdin.readline().rstrip()
cnt=0
for i in friends:
    if h==i:
        cnt+=1
print(cnt)