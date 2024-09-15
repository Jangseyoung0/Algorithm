import sys
n=sys.stdin.readline().rstrip()
num=int(n)
if '7' not in n:
    if num%7!=0:
        print(0)
    else:
        print(1)
else:
    if num%7!=0:
        print(2)
    else:
        print(3)
