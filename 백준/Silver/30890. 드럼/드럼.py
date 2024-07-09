import sys
import math
x,y=map(int,sys.stdin.readline().split())
s=math.lcm(x,y)
xi=s//x
yi=s//y
for i in range(1,s+1):
    if i%xi==0 and i%yi==0:
        print('3',end='')
    elif i%xi==0:
        print('1',end='')
    elif i%yi==0:
        print('2',end='')