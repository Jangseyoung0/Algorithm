import sys
n,*s=sys.stdin.read().split()
for i in range(int(n)):
    s[i]=s[i][::-1]
s=list(map(int,s))
print(*sorted(s),sep='\n')