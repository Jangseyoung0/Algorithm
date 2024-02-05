import sys
x=int(sys.stdin.readline().strip())
y=int(sys.stdin.readline().strip())
answer=0
if x>0:
    if y>0:
        answer=1
    else:
        answer=4
else:
    if y>0:
        answer=2
    else:
        answer=3
print(answer)