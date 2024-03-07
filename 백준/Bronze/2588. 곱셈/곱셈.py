import sys
a=int(sys.stdin.readline())
b=int(sys.stdin.readline())
sum=0
for i in range(3):
    c=a*(b%10)
    b//=10
    print(c)
    sum+=c*10**i

print(sum)
