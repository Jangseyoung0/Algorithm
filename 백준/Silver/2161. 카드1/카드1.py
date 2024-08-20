import sys
from collections import deque
n=int(sys.stdin.readline())
nums=deque()
if n==0:
    print(0)
else:
    for i in range(1,n+1):
        nums.append(i)
    while len(nums)>1:
        c=nums.popleft()
        print(c,end=' ')
        nums.append(nums[0])
        del(nums[0])
        if len(nums)==1:
            break
    print(nums[0])
