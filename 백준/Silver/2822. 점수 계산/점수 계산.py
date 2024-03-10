import sys
arr=[]
index=[]
for i in range(8):
    n=int(sys.stdin.readline())
    arr.append(n)
arr2=arr[:]
arr2.sort(reverse=True)
sum=sum(arr2[0:5])
print(sum)
for i in range(5):
    if arr2[i] in arr:
        index.append(arr.index(arr2[i])+1)
index.sort()
print(*index)