import sys
t,s=map(int,sys.stdin.readline().split())
if s==1 or t<12 or t>16:
    print(280)
else:
    print(320)
