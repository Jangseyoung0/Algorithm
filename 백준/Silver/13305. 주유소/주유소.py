import sys
n=int(sys.stdin.readline())
lens=list(map(int,sys.stdin.readline().split()))
prices=list(map(int,sys.stdin.readline().split()))
minprice=prices[0]
sum=0
for i in range(n-1):
    if minprice>prices[i]:
        minprice=prices[i]
    sum+=(minprice*lens[i])
print(sum)
            