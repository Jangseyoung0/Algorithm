import sys
n,b=sys.stdin.readline().rstrip().split()
b=int(b)
num=0
for i in range(len(n)-1,-1,-1):
    if n[i].isalpha():
        num+=((10+ord(n[i])-ord('A'))*(b**(len(n)-1-i)))
    else:
        num+=(int(n[i])*(b**(len(n)-1-i)))
print(num)