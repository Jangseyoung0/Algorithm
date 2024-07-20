import sys
from collections import deque
a,b=map(int,sys.stdin.readline().split())
q=deque([(a,1)])
while q:
    n, cnt=q.popleft()
    if n==b:
        print(cnt)
        break
    if n*2<=b:
        q.append((n*2,cnt+1))
    if n*10+1<=b:
        q.append((n*10+1,cnt+1))
else:
    print(-1)