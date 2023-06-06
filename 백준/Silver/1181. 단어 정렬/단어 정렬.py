import sys
n=int(sys.stdin.readline())
arr=[str(sys.stdin.readline().strip()) for _ in range(n)]
arr=sorted(list(set(arr)))
arr.sort(key=len)

for i in arr:
    print(i)