import sys
from collections import deque
n=int(sys.stdin.readline())
bli=list(map(int,sys.stdin.readline().split()))
balloons=deque(enumerate(bli, start=1))
result=[]
while balloons:
    idx,val=balloons.popleft()
    result.append(idx)
    if val>0:
        balloons.rotate(-(val-1))
    else:
        balloons.rotate(-val)
print(*result,sep=' ')

