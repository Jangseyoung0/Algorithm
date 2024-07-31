import sys
n=int(sys.stdin.readline())
stair=[]
for i in range(n):
    stair.append(int(sys.stdin.readline().rstrip()))
if n==1:
    print(stair[0])
elif n==2:
    print(stair[0]+stair[1])
else:
    dp=[stair[0],stair[1]+stair[0],max(stair[2]+stair[1],stair[2]+stair[0])]
    for i in range(3,n):
        dp.append(max((stair[i]+stair[i-1]+dp[i-3]),(stair[i]+dp[i-2])))
    print(dp[n-1])