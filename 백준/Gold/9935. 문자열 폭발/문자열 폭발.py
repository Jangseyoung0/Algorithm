import sys
s=list(sys.stdin.readline().rstrip())
bomb=list(sys.stdin.readline().rstrip())
len=len(bomb)
stack=[]
for i in s:
    stack.append(i)
    if stack[-len:]==bomb:
        for j in range(len):
            stack.pop()
if stack!=[]:
    print(*stack,sep='')
else:
    print("FRULA")