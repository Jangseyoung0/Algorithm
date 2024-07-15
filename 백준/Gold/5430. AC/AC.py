import sys
from collections import deque
t=int(sys.stdin.readline())
for _ in range(t):
    p=sys.stdin.readline().rstrip()
    n=int(sys.stdin.readline())
    arr=sys.stdin.readline().rstrip()[1:-1].split(',')
    l=deque(arr)
    if n==0:
        if 'D' in p:
            print('error')
        else:
            print('[]')
        continue
    rcnt=0
    for i in p:
        if i=='R':
            rcnt+=1     
        if i=='D':
            if len(l)>0:
                if rcnt%2==0:
                    l.popleft()
                else:
                    l.pop()
            else:
                print("error")
                break
    else:
        if rcnt%2==0:
            print('['+','.join(l)+']')
        else:
            l.reverse()
            print('['+','.join(l)+']')
    